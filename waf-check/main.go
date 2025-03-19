package main

import (
	"fmt"
	"log"
	"time"
)

func main() {
	config, err := LoadConfig()
	if err != nil {
		log.Fatalf("error loading configuration file '%s': %s", config.path, err)
	}

	if err := createFolder(config.OutputFolder); err != nil {
		log.Fatalf("error creating output folder: %s", err)
	}

	var filesList []string
	if config.DownloadDataset {
		filesList, err = DownloadDataset(config.DatasetFolder)
		if err != nil {
			log.Fatalf("fail downloading dataset: %s", err)
		}
	} else {
		filesList, err = listJSONFiles(config.DatasetFolder)
	}

	if len(filesList) == 0 {
		log.Fatalf("No files in dataset '%s', please download with '-download'\n", config.DatasetFolder)
	}

	if config.batch {
		batches := splitIntoDirectories(filesList, config.dirCount)
		for i, batch := range batches {
			datatsetBatchPath := fmt.Sprintf("%s/dataset_%d/", config.DatasetFolder, i)
			if err := createFolder(datatsetBatchPath); err != nil {
				log.Fatalf("unable to create batch folder '%s': %s", datatsetBatchPath, err)
			}

			if err := moveFilesToDirectory(batch, datatsetBatchPath); err != nil {
				log.Fatalf("unable to copy batch to '%s': %s", datatsetBatchPath, err)
			}
		}

		fmt.Printf("%d files have been splitted in %d folder\n", len(filesList), config.dirCount)
		return
	}

	fmt.Printf("%d files to process\n", len(filesList))

	startTime := time.Now()
	manager := NewManager(config, filesList)
	if err := manager.Run(); err != nil {
		log.Fatalf("error running manager: %s", err)
	}

	timeElapsed := time.Since(startTime)

	fmt.Printf("%v to process '%s' dataset\n", timeElapsed.Round(time.Second), config.DatasetFolder)

	if err := GetResult(manager.resultsChan, config.OutputFolder); err != nil {
		log.Fatal(err.Error())
	}

	fmt.Printf("everything went well!\n")

}
