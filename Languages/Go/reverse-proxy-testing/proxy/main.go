package main

import (
	"fmt"
	"log"
	"net/http"
	"net/http/httputil"
	"net/url"
)

var globalMux *http.ServeMux
var pythProxy *httputil.ReverseProxy

func goIndex(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Welcome to the homepage! \nYou requested: %s", r.URL.Path)
}

func goOther(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Hi You requested: %s", r.URL.Path)
}

func initializeProxy(initialURL string) *httputil.ReverseProxy {
	// Define the target backend server URL
	targetURL, err := url.Parse(initialURL)
	if err != nil {
		log.Fatal(err)
	}

	// Create the reverse proxy handler
	return httputil.NewSingleHostReverseProxy(targetURL)
}

func init() {
	globalMux = http.NewServeMux()
	pythProxy = initializeProxy("http://pyth:5787")

	globalMux.Handle("/admin/", pythProxy) // Match sub-paths like /admin/login
	globalMux.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		if r.URL.Path == "/" {
			goIndex(w, r)
			return
		}
		goOther(w, r)
	})

}

func main() {
	fmt.Printf("Starting server on port 8080")
	err := http.ListenAndServe(":8080", globalMux)
	if err != nil {
		log.Fatal(err)
	}
}
