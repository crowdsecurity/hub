package main

import (
	"encoding/base64"
	"fmt"
	"io"
	"io/ioutil"
	"log"
	"net/http"
	"os"
	"os/exec"
	"path"
	"path/filepath"
	"strconv"
	"strings"

	"gopkg.in/yaml.v2"
)

func inSlice(s string, slice []string) bool {
	for _, str := range slice {
		if str == s {
			return true
		}
	}
	return false
}

func (ti *typeInfo) generate(filepath string, configType string) (string, error) {
	pathSplit := strings.Split(filepath, "/")
	//generate doc path ?
	pdocpath := strings.Replace(filepath, ".yaml", ".md", 1)

	if pathSplit[0] != configType {
		return "", fmt.Errorf("invalid filepath %s (doesn't start with provided configType %s)", filepath, configType)
	}

	// Remove the first item (we don't need it)
	pathSplit = pathSplit[1:]

	// set user, stage and config name
	var user string
	var configName string

	switch configType {
	case "parsers", "postoverflows":
		if len(pathSplit) != 3 {
			return "", fmt.Errorf("invalid filepath '%s', should be : './%s//<user>/<scenario.yaml>'", configType, filepath)
		}
		ti.Stage = pathSplit[0]
		user = pathSplit[1]
		configName = pathSplit[2]
		configName = strings.Split(configName, ".")[0]
	case "scenarios":
		if len(pathSplit) != 2 {
			return "", fmt.Errorf("invalid filepath '%s', should be : './scenarios/<user>/<scenario.yaml>'", filepath)
		}
		user = pathSplit[0]
		configName = pathSplit[1]
		configName = strings.Split(configName, ".")[0]
	case "collections":
		if len(pathSplit) != 2 {
			return "", fmt.Errorf("invalid filepath '%s', should be : './collections/<user>/<scenario.yaml>'", filepath)
		}
		user = pathSplit[0]
		configName = pathSplit[1]
		configName = strings.Split(configName, ".")[0]

	case "data_files":
		user = pathSplit[0]
		configName = pathSplit[1]
		configName = strings.Split(configName, ".")[0]
	}
	// set the filepath
	ti.Path = filepath
	// set the author from the user
	ti.Author = user

	// set file information : autor, references, description

	/* Get description, author and references from the file */
	var fInfo fileInfo
	fileContent, err := ioutil.ReadFile(filepath)
	if err != nil {
		return "", err
	}
	if configType != "data_files" {
		err = yaml.Unmarshal(fileContent, &fInfo)
		if err != nil {
			return "", err
		}

		if fInfo.Author != "" {
			ti.Author = fInfo.Author
		}

		if !skipDataFiles {
			getDataFiles(fInfo.Data...)
		}

		if len(fInfo.References) > 0 {
			ti.References = fInfo.References
		}

		if fInfo.Description != "" {
			ti.Description = fInfo.Description
		}

		if fInfo.Labels != nil {
			ti.Labels = fInfo.Labels

			// var tags_to_keep = []string{"service", "type"}
			// for _, v := range tags_to_keep {
			// 	if x, ok := fInfo.Labels[v]; ok {
			// 		ti.Tags = append(ti.Tags, x)
			// 	}
			// }
		}

		if configType == "collections" {
			if len(fInfo.Parsers) > 0 {
				ti.Parsers = fInfo.Parsers
			}
			if len(fInfo.PostOverflows) > 0 {
				ti.PostOverflows = fInfo.PostOverflows
			}
			if len(fInfo.Scenarios) > 0 {
				ti.Scenarios = fInfo.Scenarios
			}
			if len(fInfo.Collections) > 0 {
				ti.Collections = fInfo.Collections
			}
		}
	}
	// versions informations (digest and deprecated for each version)
	if len(ti.Versions) == 0 {
		ti.Versions = make(map[string]versionInfo)
		h, err := getSHA256(filepath)
		if err != nil {
			return "", fmt.Errorf("unable to get sha256 of '%s' : %v", filepath, err)
		}
		var vInfo versionInfo
		vInfo.Digest = h
		vInfo.Deprecated = false
		ti.Versions["0.1"] = vInfo
		ti.Version = "0.1"
	} else {
		lastVersion := ti.Version
		lastDigest := ti.Versions[lastVersion].Digest
		currentDigest, err := getSHA256(filepath)
		if err != nil {
			return "", fmt.Errorf("unable to get sha256 of '%s' : %v", filepath, err)
		}
		if currentDigest != lastDigest {
			floatVersion, err := strconv.ParseFloat(ti.Version, 32)
			if err != nil {
				return "", fmt.Errorf("unable to convert version '%s' to float : %s", ti.Version, err.Error())
			}
			newVersion := fmt.Sprintf("%0.1f", floatVersion+0.1)
			ti.Version = newVersion
			log.Printf("%s new version : %s (sha:%s)", ti.Path, newVersion, currentDigest)
			var vInfo versionInfo
			vInfo.Digest = currentDigest
			vInfo.Deprecated = false
			ti.Versions[newVersion] = vInfo
		}
	}
	hubName := fmt.Sprintf("%s/%s", user, configName)
	/*if we're all good, check if markdown documentation exists and join it*/
	//pdocpath
	mdFile, err := ioutil.ReadFile(pdocpath)
	if err == nil && configType != "data_files" {
		ti.LongDescription = base64.StdEncoding.EncodeToString([]byte(string(mdFile)))
	}
	// this is to avoid HUGE indexes. We don't want to  encode mmdb inside the index for eg.
	if configType != "data_files" {
		ti.FileContent = base64.StdEncoding.EncodeToString([]byte(string(fileContent)))
	}
	return hubName, nil
}

func generateIndex(configType string) (map[string]typeInfo, error) {
	var files []string
	tInfo := make(map[string]typeInfo)
	folder := path.Join("./", configType)

	err := filepath.Walk(folder, func(path string, info os.FileInfo, err error) error {
		if configType == "data_files" || strings.HasSuffix(path, ".yaml") {
			fileInfo, err := os.Stat(path)
			if err != nil {
				log.Fatalf("Can't stat path: %v", err)
			}
			if !fileInfo.IsDir() {
				files = append(files, path)
			}
		}
		return nil
	})

	if err != nil {
		panic(err)
	}

	for _, filepath := range files {
		if strings.HasPrefix(filepath, folder) {
			var info typeInfo
			var hubName string
			var err error
			hubName, err = info.generate(filepath, configType)
			if err != nil {
				fmt.Printf("skipping '%s' because : %s\n", filepath, err.Error())
			} else {
				tInfo[hubName] = info
			}
		}
	}
	return tInfo, nil
}

// Given a path to config
func getDataFiles(dataFileCfgs ...dataFileConfig) {
	for _, dataFileCfg := range dataFileCfgs {
		fmt.Println("Downloading file from " + dataFileCfg.SourceURL)
		resp, err := http.DefaultClient.Get(
			dataFileCfg.SourceURL,
		)
		if err != nil {
			log.Fatalf("Unable to download %s : %v", dataFileCfg.SourceURL, err)
		}

		dataFileCfg.DestFile = path.Join("./data_files", dataFileCfg.DestFile)
		dir, _ := path.Split(dataFileCfg.DestFile)

		err = os.MkdirAll(dir, 0700)
		if err != nil {
			log.Fatalf("Unable to create directory: %v", err)
		}

		data, err := io.ReadAll(resp.Body)
		if err != nil {
			log.Fatalf("Unable to read response body: %v", err)
		}
		err = os.WriteFile(dataFileCfg.DestFile, data, 0644)
		if err != nil {
			log.Fatalf("Unable to write to file: %v", err)
		}
		err = processDataFile(dataFileCfg)
		if err != nil {
			log.Fatalf("Unable to process data file: %v", err)
		}

	}
}

func processDataFile(datafileCfg dataFileConfig) error {
	dfName := getDataFileNameFromPath(datafileCfg.DestFile)
	globPattern := "./data_file_scripts/" + dfName + ".*"
	globMatches, err := filepath.Glob(globPattern)
	if err != nil {
		return err
	}
	if len(globMatches) > 1 {
		return fmt.Errorf("multiple scripts found for single data file. Glob = %s", globPattern)
	} else if len(globMatches) == 1 {
		fmt.Printf("Executing %s %s \n", globMatches[0], datafileCfg.DestFile)
		cmd := exec.Command(globMatches[0], datafileCfg.DestFile)
		err := cmd.Run()
		if err != nil {
			return err
		}
	}

	return nil
}

func getDataFileNameFromPath(p string) string {
	splits := strings.Split(p, "/")
	n := len(splits)
	author := splits[n-2]
	name := strings.Split(splits[n-1], ".")[0]
	return author + "/" + name
}
