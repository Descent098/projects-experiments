//go:debug httpmuxgo121=1
package main

import (
	"embed"
	"io/fs"
	"log"
	"net/http"
)

//go:embed index.html
var homepage embed.FS

//go:embed images/*
var images embed.FS

func main() {
	mux := http.NewServeMux()
	mux.Handle("/", http.FileServer(http.FS(homepage)))

	// Access only the "images" directory within the embedded filesystem
	imagesSubFS, err := fs.Sub(images, "images")
	if err != nil {
		log.Fatal(err)
	}

	mux.Handle("/images/", http.StripPrefix("/images/", http.FileServer(http.FS(imagesSubFS))))

	err = http.ListenAndServe(":2323", mux)

	if err != nil {
		log.Fatal(err)
	}
}
