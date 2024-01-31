package main

import (
	"crypto/sha256"
	"encoding/json"
	"flag"
	"fmt"
	"io"
	"log"
	"os"

	"github.com/crowdsecurity/crowdsec/pkg/cwhub"
)

type typeInfo struct {
	Path            string                 `json:"path"`
	Stage           string                 `json:"stage,omitempty"`
	Version         string                 `json:"version"`
	Versions        map[string]versionInfo `json:"versions"`
	LongDescription string                 `json:"long_description,omitempty"`
	FileContent     string                 `json:"content"`
	Description     string                 `json:"description,omitempty"`
	Author          string                 `json:"author,omitempty"`
	References      []string               `json:"references,omitempty"`
	Labels          map[string]interface{} `json:"labels"`
	Parsers         []string               `json:"parsers,omitempty"`
	PostOverflows   []string               `json:"postoverflows,omitempty"`
	Scenarios       []string               `json:"scenarios,omitempty"`
	AppsecRules     []string               `json:"appsec-rules,omitempty"`
	AppsecConfigs   []string               `json:"appsec-configs,omitempty"`
	Contexts        []string               `json:"contexts,omitempty"`
	Collections     []string               `json:"collections,omitempty"`
}

type fileInfo struct {
	Description   string                 `yaml:"description"`
	Author        string                 `yaml:"author"`
	References    []string               `yaml:"references"`
	Labels        map[string]interface{} `json:"labels"`
	Parsers       []string               `yaml:"parsers,omitempty"`
	PostOverflows []string               `yaml:"postoverflows,omitempty"`
	Scenarios     []string               `yaml:"scenarios,omitempty"`
	AppsecRules   []string               `yaml:"appsec-rules,omitempty"`
	AppsecConfigs []string               `yaml:"appsec-configs,omitempty"`
	Contexts      []string               `yaml:"contexts,omitempty"`
	Collections   []string               `yaml:"collections,omitempty"`
}

type versionInfo struct {
	Digest     string `json:"digest"`
	Deprecated bool   `json:"deprecated"`
}

var types = []string{
	"parsers",
	"scenarios",
	"postoverflows",
	"appsec-rules",
	"appsec-configs",
	"contexts",
	"collections",
}

func getSHA256(filepath string) (string, error) {
	/* Digest of file */
	f, err := os.Open(filepath)
	if err != nil {
		return "", fmt.Errorf("unable to open '%s' : %s", filepath, err.Error())
	}

	defer f.Close()

	h := sha256.New()
	if _, err := io.Copy(h, f); err != nil {
		return "", fmt.Errorf("unable to calculate sha256 of '%s': %s", filepath, err.Error())
	}

	return fmt.Sprintf("%x", h.Sum(nil)), nil
}

func main() {
	var generate bool
	var inputFile string
	var outFile string
	var target string

	idx := make(map[string]map[string]typeInfo)
	tmpIdx := make(map[string]map[string]typeInfo)

	flag.StringVar(&target, "target", "all", "decide what to generate : blockers|configs|all")
	flag.StringVar(&outFile, "output", ".index.json", "File to output index")
	flag.BoolVar(&generate, "generate", false, "File to output index")
	flag.StringVar(&inputFile, "input", ".index.json", "File to read index from")
	flag.Parse()

	if target == "all" || target == "configs" {
		if generate {
			for _, t := range types {
				configType, err := generateIndex(t)
				if err != nil {
					panic(err)
				}
				idx[t] = configType
			}
		} else {
			// update .index file
			f, _ := os.ReadFile(inputFile)

			_ = json.Unmarshal([]byte(f), &tmpIdx)

			for _, t := range types {
				updateIndex(t, idx, tmpIdx)
			}
		}

		json, err := json.MarshalIndent(idx, "", " ")
		if err != nil {
			panic(err)
		}
		if err := os.WriteFile(outFile, json, 0644); err != nil {
			log.Fatalf("failed writting new json index : %s", err)
		}

		/*Check if the generated index is correct*/
		indexContent, err := os.ReadFile(outFile)
		if err != nil {
			log.Fatalf("Unable to read index : %v", err)
		}
		_, err = cwhub.LoadPkgIndex(indexContent)
		if err != nil {
			log.Fatalf("Unable to load existing index : %v.", err)
		}
	}
	if target == "all" || target == "blockers" {
		blockers, err := LoadJSON("blockers/list.json")
		if err != nil {
			log.Fatalf("failed to load json : %s", err)
		}
		log.Printf("Loaded %d blockers", len(blockers))
		for x, blocker := range blockers {
			log.Printf("%d/%d", x+1, len(blockers))

			updated, err := UpdateItem(blocker)
			if err != nil {
				log.Fatalf("failed to update %+v : %s", blocker, err)
			}
			blockers[x] = updated
		}
		log.Printf("Dumping updated items")

		if err := DumpJSON("blockers.json", blockers); err != nil {
			log.Fatalf("failed to dump new json file : %s", err)
		}
	}
}
