package main

import (
	"bytes"
	"fmt"
	"io"
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
	request.URL = fmt.Sprintf("/%s", strings.TrimLeft(request.URL, "/"))
	if strings.HasSuffix(baseURL, "/") {
		baseURL = strings.TrimRight(baseURL, "/")
	}
	request.FullURL = baseURL + request.URL

	parsedBaseURL, err := url.Parse(baseURL)
	if err != nil {
		return http.Request{}, err
	}

	parsedBaseURL.Opaque = request.URL

	req := &http.Request{
		Method: request.Method,
		Header: make(http.Header),
		URL:    parsedBaseURL,
	}

	if request.Method == http.MethodPost || request.Method == http.MethodPut {
		req.Body = io.NopCloser(strings.NewReader(request.Data))
		req.ContentLength = int64(len(request.Data))
	}

	/*if request.Method == http.MethodPost || request.Method == http.MethodPut {
		req, err = http.NewRequest(request.Method, request.FullURL, bytes.NewBufferString(request.Data))
	} else {
		req, err = http.NewRequest(request.Method, request.FullURL, http.NoBody)
	}

	if err != nil {
		return http.Request{}, err
	}*/

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
	if r.Method == http.MethodPost || r.Method == http.MethodPut {
		curlCmd.WriteString(fmt.Sprintf(" -d '%s'", r.Data))
	}
	curlCmd.WriteString(fmt.Sprintf(" '%s'", r.FullURL))

	return curlCmd.String()
}
