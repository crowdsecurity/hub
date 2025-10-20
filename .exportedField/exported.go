package main

import (
	"log"
	"maps"
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
		results = []types.Event{}
		final   = types.Event{
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
			if buf, err = os.ReadFile(path); err != nil {
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
		maps.Copy(final.Enriched, result.Enriched)
		maps.Copy(final.Parsed, result.Parsed)
		maps.Copy(final.Meta, result.Meta)
	}

	if buf, err = yaml.Marshal(final); err != nil {
		log.Printf("Unable to marshal result: %s", err)
	}

	if err = os.WriteFile("exportedField.yaml", buf, 0o644); err != nil {
		log.Printf("Unable to write file: %s", err)
	}
}
