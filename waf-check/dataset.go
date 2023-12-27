package main

import (
	"fmt"
	"os"
)

const (
	datasetURL = "https://downloads.openappsec.io/waf-comparison-project/legitimate.zip"
)

func DownloadDataset(datasetFolder string) ([]string, error) {
	fmt.Printf("Downloading dataset to '%s'\n", datasetFolder)
	file, err := downloadFile(datasetURL)
	if err != nil {
		return []string{}, err
	}
	fmt.Printf("File downloaded from '%s'\n", datasetURL)
	fmt.Printf("Unzipping '%s' into '%s'\n", file.Name(), datasetFolder)
	err = unzip(file.Name(), datasetFolder)
	if err != nil {
		return []string{}, err
	}

	file.Close()
	os.Remove(file.Name())

	fmt.Printf("Dataset successfully downloaded to '%s'\n", datasetFolder)

	return listJSONFiles(datasetFolder)
}
