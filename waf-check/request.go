package main

import (
	"bytes"
	"fmt"
	"net/http"
	"net/url"
	"strings"
)

type Response struct {
	URL        string              `json:"url"`
	StatusCode int                 `json:"status_code"`
	Headers    map[string][]string `json:"headers"`
	Body       string              `json:"body"`
}

type Request struct {
	Headers map[string]string `json:"headers"`
	Method  string            `json:"method"`
	Data    string            `json:"data"`
	URL     string            `json:"url"`
	FullURL string            `json:"-"`
}

func NewHTTPRequest(baseURL string, request *Request) (http.Request, error) {
	var req *http.Request
	var err error

	parsedBaseURL, err := url.Parse(baseURL)
	if err != nil {
		return *req, fmt.Errorf("error parsing base URL: %w", err)
	}

	request.URL = fmt.Sprintf("/%s", strings.TrimLeft(request.URL, "/"))

	parsedURI, err := url.Parse(request.URL)
	if err != nil {
		return *req, fmt.Errorf("error parsing URI: %w", err)
	}

	request.FullURL = parsedBaseURL.ResolveReference(parsedURI).String()

	if request.Method == "POST" || request.Method == "PUT" {
		req, err = http.NewRequest(request.Method, request.FullURL, bytes.NewBufferString(request.Data))
	} else {
		req, err = http.NewRequest(request.Method, request.FullURL, nil)
	}

	if err != nil {
		return *req, err
	}

	for key, value := range request.Headers {
		req.Header.Add(key, value)
	}

	return *req, nil
}

func (r *Request) Curl() string {
	var curlCmd bytes.Buffer

	curlCmd.WriteString("curl -X " + r.Method)

	for key, value := range r.Headers {
		curlCmd.WriteString(fmt.Sprintf(" -H '%s: %s'", key, value))
	}
	if r.Method == "POST" || r.Method == "PUT" {
		curlCmd.WriteString(fmt.Sprintf(" -d '%s'", r.Data))
	}
	curlCmd.WriteString(fmt.Sprintf(" '%s'", r.FullURL))

	return curlCmd.String()
}
