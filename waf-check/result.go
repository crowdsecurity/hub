package main

import (
	"encoding/json"
	"fmt"
	"log"
	"os"
	"path/filepath"
)

func GetResult(resultsChan chan Result, outputFolder string) error {
	resultCpt := 0
	totalTestRun := 0
	totalFileRun := 0
	totalTestFail := 0
	for result := range resultsChan {
		totalFileRun += 1
		totalTestRun += result.DoneTests
		totalTestFail += len(result.FailedTests)

		resultCpt += 1
		fmt.Printf("'%s' result:\n", result.Filename)
		fmt.Printf("  - %d/%d tests done\n", result.DoneTests, result.TotalTests)
		fmt.Printf("  - %d/%d tests failed\n", len(result.FailedTests), result.DoneTests)
		if len(result.FailedTests) > 0 {
			filename := filepath.Base(result.Filename)
			failedTestFile := fmt.Sprintf("failed_%s", filename)
			failedTestsPath := fmt.Sprintf("%s/%s", outputFolder, failedTestFile)

			jsonData, err := json.MarshalIndent(result, "", "  ")
			if err != nil {
				log.Fatalf("unable to marshal: %+v", result)
			}
			if err := os.WriteFile(failedTestsPath, jsonData, 0644); err != nil {
				log.Fatalf("unable to write failed report '%s': %s", failedTestsPath, err)
			}
			fmt.Printf("  - failed tests report: '%s'\n", failedTestsPath)
		}
		if resultCpt == cap(resultsChan) {
			break
		}
	}
	close(resultsChan)

	fmt.Println("Result:")
	fmt.Printf("  - Total file: %d\n", totalFileRun)
	fmt.Printf("  - Total test: %d\n", totalTestRun)
	fmt.Printf("  - Total fail: %d\n", totalTestFail)

	return nil
}
