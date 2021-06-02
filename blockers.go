package main

import (
	"context"
	"encoding/base64"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"time"

	"github.com/google/go-github/github"
	"github.com/pkg/errors"
)

const (
	npmAPIMaxDurationMonth = 17 // in month
)

var (
	expressBouncerReleaseDateTime = time.Date(2020, 01, 01, 0, 0, 0, 0, time.UTC)
)

type npmAPIDownloadResponse struct {
	Downloads int `json:"downloads"`
}

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

func fetchExpressBouncerDownloadFromDate(startDate time.Time, endDate time.Time) (int, error) {
	url := fmt.Sprintf("https://api.npmjs.org/downloads/point/%s:%s/@crowdsec/express-bouncer", fmt.Sprintf("%d-%d-%d", startDate.Year(), startDate.Month(), startDate.Day()), fmt.Sprintf("%d-%d-%d", endDate.Year(), endDate.Month(), endDate.Day()))

	req, err := http.NewRequest("GET", url, nil)
	if err != nil {
		return 0, errors.Wrapf(err, "creating request to fetch downloads from NPM API")
	}
	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		return 0, errors.Wrapf(err, "doing request to fetch downloads from NPM API")
	}
	if resp.Body == nil {
		return 0, fmt.Errorf("response from NPM API is empty")
	}
	defer resp.Body.Close()

	body, readErr := ioutil.ReadAll(resp.Body)
	if readErr != nil {
		return 0, errors.Wrapf(err, "reading body while fetching downloads from NPM API")
	}
	npmResp := npmAPIDownloadResponse{}
	if err := json.Unmarshal(body, &npmResp); err != nil {
		return 0, errors.Wrapf(err, "unmarshaling body while fetching downloads from NPM API")
	}

	return npmResp.Downloads, nil
}

func fetchExpressBouncerDownload() (int, error) {
	var totalDownload int
	startDate := expressBouncerReleaseDateTime
	endDate := startDate.AddDate(0, npmAPIMaxDurationMonth, 0)

	now := time.Now()

	for {
		if endDate.After(now) {
			nbDownload, err := fetchExpressBouncerDownloadFromDate(startDate, now)
			if err != nil {
				return 0, err
			}
			totalDownload += nbDownload
			break
		}
		nbDownload, err := fetchExpressBouncerDownloadFromDate(startDate, endDate)
		if err != nil {
			return 0, err
		}
		totalDownload += nbDownload
		startDate = endDate
		endDate = startDate.AddDate(0, npmAPIMaxDurationMonth, 0)

	}

	return totalDownload, nil
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
	if item.Name == "cs-express-bouncer" {
		nbDownload, err := fetchExpressBouncerDownload()
		if err != nil {
			return item, err
		}
		item.DownloadCount += nbDownload
	}

	/*get infos about latest release*/
	release, _, _ := client.Repositories.GetLatestRelease(context.Background(), item.Owner, item.Name)
	if release != nil {
		item.LastVersion = *release.TagName
		log.Printf("LastVersion : %s", item.LastVersion)
		item.DownloadURL = release.GetHTMLURL()
		log.Printf("DownloadURL : %s", item.DownloadURL)
		log.Printf("len(assets) : %d", len(release.Assets))
		if len(release.Assets) > 0 {
			item.AssetURL = release.Assets[0].GetBrowserDownloadURL()
		} else {
			item.AssetURL = *release.ZipballURL
		}
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
