package main

import (
	"flag"
	"fmt"
	"net/http"
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
	statusCode      int    `yaml:"-"`
	path            string `yaml:"-"`
	batch           bool   `yaml:"-"`
	dirCount        int    `yaml:"-"`
}

func LoadConfig() (Config, error) {
	var config Config

	configFile := flag.String("config", "./config.yaml", "Configuration file")
	datasetFolder := flag.String("dataset", "", "Path to dataset. Priority over configuration file")
	outputFolder := flag.String("output", "", "Path to fail directory. Priority over configuration file")
	batch := flag.Bool("batch", false, "Batch mode")
	download := flag.Bool("download", false, "Download dataset. Priority over configuration file")
	dirCount := flag.Int("dir-count", 3, "Split batch")
	statusCode := flag.Int("status-code", http.StatusForbidden, "Expected status code")
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

	if *outputFolder != "" {
		config.OutputFolder = *outputFolder
	}

	if *datasetFolder != "" {
		config.DatasetFolder = *datasetFolder
	}

	if *download {
		config.DownloadDataset = *download
	}

	config.batch = *batch
	config.dirCount = *dirCount
	config.statusCode = *statusCode

	return config, nil
}
