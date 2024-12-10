package main

import (
	"golang-testing/api"
	"net/http"
)

func main() {
	mux := api.SetupServer()
	// Run
	http.ListenAndServe(":8090", mux)
}
