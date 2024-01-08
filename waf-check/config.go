package main

import (
	"flag"
	"fmt"
	"os"

	"gopkg.in/yaml.v2"
)

type Config struct {
	WafURL          string `yaml:"waf_url"`
	TestName        string `yaml:"name"`
	DatasetFolder   string `yaml:"dataset_folder"`
	NbRoutines      int    `yaml:"nb_routines"`
	OutputFolder    string `yaml:"output_folder"`
	DownloadDataset bool   `yaml:"download_dataset"`
	path            string `yaml:"-"`
	batch           bool   `yaml:"-"`
	dirCount        int    `yaml:"-"`
}

func LoadConfig() (Config, error) {
	var config Config

	configFile := flag.String("config", "./config.yaml", "Configuration file")
	datasetFolder := flag.String("dataset", "", "Path to dataset. Priority over configuration file")
	batch := flag.Bool("batch", false, "Batch mode")
	download := flag.Bool("download", false, "Download dataset")
	dirCount := flag.Int("dir-count", 3, "Split batch")
	flag.Parse()

	config.path = *configFile

	data, err := os.ReadFile(*configFile)
	if err != nil {
		return config, fmt.Errorf("error reading YAML file: %s", err)
	}

	err = yaml.Unmarshal(data, &config)
	if err != nil {
		return config, fmt.Errorf("error unmarshaling YAML: %s", err)
	}

	if *datasetFolder != "" {
		config.DatasetFolder = *datasetFolder
	}

	if *download {
		config.DownloadDataset = *download
	}

	config.batch = *batch
	config.dirCount = *dirCount

	return config, nil
}
