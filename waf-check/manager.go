package main

import (
	"encoding/json"
	"fmt"
	"io"
	"log"
	"net/http"
	"os"
	"sync"
	"time"
)

type Manager struct {
	filesChan   chan string
	resultsChan chan Result
	wg          *sync.WaitGroup
	WafURL      string
	NbWorker    int
	filesList   []string
	statusCode  int
}

type FailTest struct {
	Request     Request  `json:"request"`
	Response    Response `json:"response"`
	CurlCommand string   `json:"curl"`
	Error       string   `json:"error"`
}

type Result struct {
	TotalTests  int
	FailedTests []FailTest
	DoneTests   int
	Filename    string
}

func (m *Manager) processFile(file string) {
	defer m.wg.Done()

	jsonData, err := os.ReadFile(file)
	if err != nil {
		log.Fatalf("error reading request file: %s\n", err)
	}

	var requests []Request
	if err := json.Unmarshal(jsonData, &requests); err != nil {
		log.Fatalf("error unmarshalling request file '%s': %s", file, err)
	}

	client := &http.Client{Timeout: 3 * time.Second}

	result := Result{
		Filename:    file,
		TotalTests:  len(requests),
		DoneTests:   0,
		FailedTests: make([]FailTest, 0),
	}

	for _, request := range requests {
		req, err := NewHTTPRequest(m.WafURL, &request)
		if err != nil {
			log.Fatalf("error creating http request for file '%s': %s", file, err)
		}

		resp, err := client.Do(&req)
		if err != nil {
			log.Fatalf("error doing request from file '%s' to '%s': %s", file, request.FullURL, err)
		}

		if resp.StatusCode == m.statusCode {
			readErr := ""
			responseBody, err := io.ReadAll(resp.Body)
			if err != nil {
				readErr = fmt.Sprintf("error reading response body for URL %s: %s\n", request.FullURL, err)
				fmt.Println(readErr)
			}
			response := Response{
				URL:        request.URL,
				StatusCode: resp.StatusCode,
				Headers:    resp.Header,
				Body:       string(responseBody),
			}
			failedTest := FailTest{
				Request:     request,
				Response:    response,
				CurlCommand: request.Curl(),
				Error:       readErr,
			}
			result.FailedTests = append(result.FailedTests, failedTest)
		}
		resp.Body.Close()
		result.DoneTests += 1

	}

	m.resultsChan <- result

}

func NewManager(config Config, filesList []string) Manager {
	return Manager{
		WafURL:      config.WafURL,
		NbWorker:    config.NbRoutines,
		wg:          &sync.WaitGroup{},
		filesChan:   make(chan string),
		resultsChan: make(chan Result, len(filesList)),
		filesList:   filesList,
		statusCode:  config.statusCode,
	}
}

func (m *Manager) Run() error {
	for i := 0; i < m.NbWorker; i++ {
		go func() {
			for file := range m.filesChan {
				m.processFile(file)
			}
		}()
	}

	fmt.Printf("%d workers started (processing %d files)\n", m.NbWorker, len(m.filesList))

	m.wg.Add(len(m.filesList))

	for _, file := range m.filesList {
		m.filesChan <- file
	}
	close(m.filesChan)

	m.wg.Wait()
	return nil
}
