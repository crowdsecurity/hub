package main

import (
	"archive/zip"
	"fmt"
	"io"
	"io/fs"
	"net/http"
	"os"
	"path/filepath"
	"strings"
)

func listJSONFiles(folderPath string) ([]string, error) {
	filesList := make([]string, 0)
	err := filepath.Walk(folderPath, func(path string, info fs.FileInfo, err error) error {
		if err != nil {
			return err
		}
		if !info.IsDir() && strings.HasSuffix(info.Name(), ".json") {
			filesList = append(filesList, path)
		}
		return nil
	})

	if err != nil {
		return filesList, fmt.Errorf("error walking '%s': %s", folderPath, err)
	}

	return filesList, nil
}

func createFolder(folderPath string) error {
	if _, err := os.Stat(folderPath); os.IsNotExist(err) {
		err := os.MkdirAll(folderPath, os.ModePerm)
		if err != nil {
			return fmt.Errorf("error creating directory: %w", err)
		}
	} else if err != nil {
		return fmt.Errorf("error checking directory: %w", err)
	}

	return nil
}

func downloadFile(url string) (*os.File, error) {
	resp, err := http.Get(url)
	if err != nil {
		return nil, err
	}
	defer resp.Body.Close()

	tmpFile, err := os.CreateTemp("", "archive-*.zip")
	if err != nil {
		return nil, err
	}

	_, err = io.Copy(tmpFile, resp.Body)
	if err != nil {
		tmpFile.Close()
		return nil, err
	}

	return tmpFile, nil
}

func unzip(src, dest string) error {
	r, err := zip.OpenReader(src)
	if err != nil {
		return err
	}
	defer r.Close()

	os.MkdirAll(dest, 0755)

	for _, f := range r.File {
		fPath := filepath.Join(dest, f.Name)
		fmt.Printf("Extracting '%s' \n", fPath)

		// create the folder of the file if doesn't exist
		folderPath := filepath.Dir(fPath)
		os.MkdirAll(folderPath, os.ModePerm)

		outFile, err := os.OpenFile(fPath, os.O_WRONLY|os.O_CREATE|os.O_TRUNC, os.ModePerm)
		if err != nil {
			return err
		}

		rc, err := f.Open()
		if err != nil {
			outFile.Close()
			return err
		}

		_, err = io.Copy(outFile, rc)

		outFile.Close()
		rc.Close()

		if err != nil {
			return err
		}
	}
	return nil
}

func splitIntoDirectories(files []string, dirCount int) [][]string {
	var directories [][]string
	totalFiles := len(files)
	minFilesPerDir := totalFiles / dirCount
	extraFiles := totalFiles % dirCount

	start := 0
	for i := 0; i < dirCount; i++ {
		end := start + minFilesPerDir
		if i < extraFiles {
			end++
		}

		directories = append(directories, files[start:end])
		start = end
	}

	return directories
}

func moveFile(src, dst string) error {
	err := os.Rename(src, dst)
	if err != nil {
		return fmt.Errorf("failed to move %s to %s: %w", src, dst, err)
	}
	return nil
}

func moveFilesToDirectory(files []string, destDir string) error {
	for _, file := range files {
		fileName := filepath.Base(file)
		destPath := filepath.Join(destDir, fileName)

		err := moveFile(file, destPath)
		if err != nil {
			return err
		}
	}
	return nil
}
