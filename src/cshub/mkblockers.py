import base64
import json
import os
from dataclasses import asdict, dataclass, field
from datetime import datetime, timedelta
from pathlib import Path

import requests
from github import Github

NPM_API_MAX_DURATION_MONTH = 17
EXPRESS_BOUNCER_RELEASE_DATE = datetime(2021, 1, 1)


def add_subparser(subparsers):
    parser = subparsers.add_parser("mkblockers", description="Create blockers.json")
    parser.add_argument("--out", default="blockers.json", type=str,
                        help="The json file to write")
    return parser


@dataclass
class ItemInfo:
    name: str
    author: str
    logo: str
    url: str = ""
    description: str = ""
    stars: int = 0
    downloads: int = 0
    readme_content: str = ""
    status: str = ""
    version: str = ""
    release_date: str = ""
    assets: list[dict] = field(default_factory=list)

    def to_dict(self):
        return asdict(self)


def fetch_express_bouncer_download_from_date(
    start_date: datetime, end_date: datetime,
) -> int:
    url = f"https://api.npmjs.org/downloads/point/{start_date.strftime('%Y-%m-%d')}:{end_date.strftime('%Y-%m-%d')}/@crowdsec/express-bouncer"
    response = requests.get(url)
    response.raise_for_status()
    return response.json().get("downloads", 0)


def fetch_express_bouncer_download() -> int:
    total_downloads = 0
    start_date = EXPRESS_BOUNCER_RELEASE_DATE
    now = datetime.now()

    while start_date < now:
        end_date = min(
            start_date + timedelta(days=NPM_API_MAX_DURATION_MONTH * 30), now,
        )
        total_downloads += fetch_express_bouncer_download_from_date(
            start_date, end_date,
        )
        start_date = end_date

    return total_downloads


def load_json(file: str) -> list[ItemInfo]:
    with Path(file).open() as f:
        data = json.load(f)
    return [ItemInfo(**item) for item in data]


def default_assets(latest_release, repo_url: str) -> list[dict]:
    if latest_release.assets:
        return [
            {
                "name": asset.name,
                "download_url": asset.browser_download_url,
                "asset_url": asset.url,
            }
            for asset in latest_release.assets
        ]
    return [
        {
            "name": "Tarball (source code)",
            "download_url": latest_release.tarball_url,
            "asset_url": latest_release.tarball_url,
        },
        {
            "name": "Zipball (source code)",
            "download_url": latest_release.zipball_url,
            "asset_url": latest_release.zipball_url,
        },
    ]


def update_item(item: ItemInfo, github_client: Github) -> ItemInfo:
    print(f"Updating {item.author}/{item.name}")
    repo = github_client.get_repo(f"{item.author}/{item.name}")

    item.stars = repo.stargazers_count
    item.url = repo.html_url
    item.description = repo.description or ""
    item.readme_content = base64.b64encode(repo.get_readme().decoded_content).decode(
        "utf-8",
    )

    releases = repo.get_releases()
    if releases.totalCount > 0:
        latest_release = next(
            (release for release in releases if not release.prerelease), releases[0],
        )
        item.status = "stable" if not latest_release.prerelease else "unstable"
        item.version = latest_release.tag_name
        item.assets = default_assets(latest_release, repo.html_url)
        item.downloads = sum(
            asset.download_count for release in releases for asset in release.assets
        )
        item.release_date = latest_release.published_at.strftime("%Y-%m-%dT%H:%M:%SZ")
    else:
        item.status = "development"
        item.version = "no release"
        item.assets = [
            {
                "name": "no release",
                "download_url": repo.html_url + "/tags",
                "asset_url": repo.html_url + "/tags",
            },
        ]

    if item.name == "cs-express-bouncer":
        item.downloads += fetch_express_bouncer_download()

    return item


def main(args):
    blockers = load_json("blockers/list.json")
    print(f"Loaded {len(blockers)} blockers")

    github_token = os.getenv("GH_TOKEN")
    github_client = Github(github_token) if github_token else Github()

    for i, blocker in enumerate(blockers):
        print(f"{i + 1}/{len(blockers)}")
        blockers[i] = update_item(blocker, github_client)

    with Path(args.out).open("w") as f:
        print(f"Writing to {args.out}")
        json.dump([item.to_dict() for item in blockers], f, indent=2, sort_keys=True)
