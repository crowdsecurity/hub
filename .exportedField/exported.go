package main

import (
	"io/ioutil"
	"log"
	"os"
	"path/filepath"

	"github.com/crowdsecurity/crowdsec/pkg/types"
	"gopkg.in/yaml.v2"
)

type ParserResults struct {
	ProvisionalResults []map[string]map[string]types.Event
	FinalResults       []types.Event
}

func main() {
	var (
		buf     []byte
		err     error
		results []types.Event = []types.Event{}
		final   types.Event   = types.Event{
			Enriched: map[string]string{},
			Parsed:   map[string]string{},
			Meta:     map[string]string{},
		}
	)
	_ = filepath.Walk(".", func(path string, info os.FileInfo, err error) error {
		if err != nil {
			log.Printf("prevent panic by handling failure accessing a path %q: %v\n", path, err)
			return err
		}
		if !info.IsDir() && info.Name() == "parser_results.yaml" {
			if buf, err = ioutil.ReadFile(path); err != nil {
				log.Printf("Unable to read %s: %s", path, err)
				return err
			}
			tmp := ParserResults{}
			if err = yaml.Unmarshal(buf, &tmp); err != nil {
				log.Printf("Unable to unmarshal path %s: %s", path, err)
			}
			results = append(results, tmp.FinalResults...)
		}
		return nil

	})

	for _, result := range results {
		for key, value := range result.Enriched {
			final.Enriched[key] = value
		}
		for key, value := range result.Parsed {
			final.Parsed[key] = value
		}
		for key, value := range result.Meta {
			final.Meta[key] = value
		}
	}

	if buf, err = yaml.Marshal(final); err != nil {
		log.Printf("Unable to marshal result: %s", err)
	}

	if err = ioutil.WriteFile("exportedField.yaml", buf, 0644); err != nil {
		log.Printf("Unable to write file: %s", err)
	}
}
