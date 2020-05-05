package main

import (
	"fmt"
	"log"
	"os"
	"path"
	"path/filepath"
	"strings"
)

func updateType(name string, dict map[string]typeInfo, filepath string, configType string) typeInfo {
	var tInfo typeInfo
	tInfo = dict[name]
	tInfo.generate(filepath, configType)
	return tInfo
}

func updateIndex(configType string, idx map[string]map[string]typeInfo, tmpIdx map[string]map[string]typeInfo) {
	var files []string
	//tInfo := make(map[string]typeInfo)
	folder := path.Join("./", configType)

	idx[configType] = make(map[string]typeInfo)

	err := filepath.Walk(folder, func(path string, info os.FileInfo, err error) error {
		if strings.HasSuffix(path, ".yaml") {
			files = append(files, path)
		}
		return nil
	})

	if err != nil {
		panic(err)
	}

	log.Printf("Updating stuff for %s", configType)
	for _, filepath := range files {
		var foundFile bool
		foundFile = false
		// only deal with filepath that starts with parsers/scenarios/postoverflows
		if strings.HasPrefix(filepath, folder) {
			// we are going to check if the file is already in the index to update it
			if val, ok := tmpIdx[configType]; ok {
				var tInfo typeInfo
				var hubName string
				for name, info := range val {
					if filepath == info.Path {
						tInfo = updateType(name, val, filepath, configType)
						hubName = name
						foundFile = true
						break
					}
				}
				if foundFile {
					idx[configType][hubName] = tInfo
				} else {
					// the file was not found in the .index, creating a new entry
					var tInfo typeInfo
					hubName, err := tInfo.generate(filepath, configType)
					if err != nil {
						fmt.Printf("skipping '%s' because : %s\n", filepath, err.Error())
					} else {
						idx[configType][hubName] = tInfo
					}
				}
			}
		}
	}
}
