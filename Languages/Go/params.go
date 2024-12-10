package main

import (
	"fmt"
	"net/http"
)

// Query Params
func contact(writer http.ResponseWriter, request *http.Request) {
	values := request.URL.Query()
	fmt.Printf("Values: %v", values)
}

// Path Params
func weather(writer http.ResponseWriter, request *http.Request) {
	city := request.PathValue("city")
	fmt.Printf("City: %v", city)
}

func main() {
	// Setup server
	mux := http.NewServeMux()

	// Add routes
	mux.HandleFunc("/contact", contact)
	mux.HandleFunc("/weather/{city}", weather)

	// Run
	http.ListenAndServe(":8090", mux)
}
