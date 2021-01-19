package main

import (
	"context"
	"encoding/base64"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"

	"github.com/google/go-github/github"
)

type ItemInfo struct {
	//Source info (crafted by humans)
	Name  string `json:"name"`
	Owner string `json:"author"`
	Logo  string `json:"logo"`
	//Main infos about repo
	URL           string `json:"url"`
	Description   string `json:"description"`
	Stargazers    int    `json:"stars"`
	DownloadCount int    `json:"downloads"`
	ReadmeContent string `json:"readme_content"`
	//Infos about last downloadable version
	LastVersion string `json:"version"`
	DownloadURL string `json:"download_url"`
	AssetURL    string `json:"asset_url"`
	Status      string `json:"status"`
}

//DumpJSON dumps the list to a json file
func DumpJSON(file string, items []ItemInfo) error {
	dump, err := json.MarshalIndent(items, "", " ")
	if err != nil {
		return fmt.Errorf("failed to unmarshal : %s", err)
	}
	err = ioutil.WriteFile(file, dump, 0755)
	if err != nil {
		return fmt.Errorf("failed to write dump : %s", err)
	}
	return nil
}

//LoadJSON loads a list of blockers from json
func LoadJSON(file string) ([]ItemInfo, error) {
	var blockers []ItemInfo
	body, err := ioutil.ReadFile(file)
	if err != nil {
		return nil, fmt.Errorf("failed to open %s : %s", file, err)
	}
	if err = json.Unmarshal(body, &blockers); err != nil {
		return nil, fmt.Errorf("failed to decode json : %s", err)
	}
	return blockers, nil
}

//UpdateItem refreshes the item information from github api
func UpdateItem(item ItemInfo) (ItemInfo, error) {
	/*Configure client with auth*/
	client := github.NewClient(nil)
	/*get main infos about repo*/
	log.Printf("updating %s/%s", item.Owner, item.Name)
	repinfo, _, err := client.Repositories.Get(context.Background(), item.Owner, item.Name)
	if err != nil {
		return item, fmt.Errorf("unable to get %s/%s : %s", item.Owner, item.Name, err)
	}
	item.Stargazers = repinfo.GetStargazersCount()
	log.Printf("Stargazers : %d", item.Stargazers)
	item.URL = repinfo.GetHTMLURL()
	log.Printf("URL : %s", item.URL)
	item.Description = repinfo.GetDescription()
	log.Printf("Description : %s", item.Description)

	/*get the readme*/
	readme, _, err := client.Repositories.GetReadme(context.Background(), item.Owner, item.Name, nil)
	if err != nil {
		return item, fmt.Errorf("Failed to get the readme : %s", err)
	}

	content, err := readme.GetContent()
	if err != nil {
		return item, fmt.Errorf("Failed to get the readme content : %s", err)
	}
	log.Printf("len(readme) : %d", len(content))
	item.ReadmeContent = base64.StdEncoding.EncodeToString([]byte(content))

	// Fetch nb downloads of all (pre-)releases
	releases, _, err := client.Repositories.ListReleases(context.Background(), item.Owner, item.Name, nil)
	if err != nil {
		log.Fatalf("Failed to fetch releases : %+v", err.Error())
	}
	if len(releases) > 0 {
		/*get download count*/
		for _, release := range releases {
			for x, asset := range release.Assets {
				if x == 0 {
					item.AssetURL = asset.GetBrowserDownloadURL()
					log.Printf("AssetURL : %s", item.AssetURL)
				}
				item.DownloadCount += asset.GetDownloadCount()
			}
		}
	}

	/*get infos about latest release*/
	release, _, _ := client.Repositories.GetLatestRelease(context.Background(), item.Owner, item.Name)
	if release != nil {
		item.LastVersion = *release.TagName
		log.Printf("LastVersion : %s", item.LastVersion)
		item.DownloadURL = release.GetHTMLURL()
		log.Printf("DownloadURL : %s", item.DownloadURL)
		log.Printf("len(assets) : %d", len(release.Assets))
		item.AssetURL = release.Assets[0].GetBrowserDownloadURL()
		item.Status = "stable"
	} else {
		/*if has prerelease*/
		releases, _, err := client.Repositories.ListReleases(context.Background(), item.Owner, item.Name, nil)
		if err != nil {
			log.Fatalf("Failed to fetch releases : %+v", err.Error())
		}
		if len(releases) > 0 {
			item.DownloadURL = *releases[0].HTMLURL
			item.LastVersion = *releases[0].TagName
			item.Status = "unstable"
			log.Printf("Has only prereleases : %s", item.DownloadURL)
			log.Printf("LastVersion : %s", item.LastVersion)
		} else {
			item.LastVersion = "no release"
			item.DownloadURL = *repinfo.HTMLURL + "/tags"
			item.AssetURL = *repinfo.HTMLURL + "/tags"
			item.DownloadCount = 0
			item.Status = "development"
			log.Printf("Has no release : %s", item.DownloadURL)
		}
	}
	return item, nil
}
