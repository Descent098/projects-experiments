package main

/*
#include <stdlib.h>

typedef struct{
	char* url;
	char* domain;
	char* server;
	char* protocol;
	char* contentType;
	char* body;
	int port;
} Site;
*/
import "C"
import (
	"fmt"
	"io"
	"net"
	"net/http"
	"net/url"
	"time"
	"unsafe"
)

// Go-side version of the struct
type Site struct {
	url         string // the raw URL
	domain      string // The domain the URL is hosted at
	server      string // The value of the server header
	protocol    string // The protocl of the site (http or https)
	contentType string // The content type of the body (i.e. "text/html")
	body        string // The body of the url
	port        int    // The port the url is on
}

// Gets a key from headers if it's available, else returns the specified defaultvalue
func getFromHeaders(headers http.Header, key string, defaultValue string) string {
	values, ok := headers[key]
	if !ok || len(values) == 0 {
		return defaultValue
	}
	return values[0]
}

// Scrape metadata from a site
func scrapeSite(rawUrl string) (*Site, error) {
	parsedURL, err := url.Parse(rawUrl)
	if err != nil {
		return nil, err
	}

	protocol := parsedURL.Scheme
	domain := parsedURL.Hostname()
	port := 80
	if protocol == "https" {
		port = 443
	}
	if parsedURL.Port() != "" {
		p, err := net.LookupPort("tcp", parsedURL.Port())
		if err == nil {
			port = p
		}
	}

	client := &http.Client{
		Timeout: 2 * time.Second, // Set timeout to 2 seconds
	}

	resp, err := client.Get(rawUrl)
	if err != nil {
		return nil, err
	}
	defer resp.Body.Close()

	bodyBytes, err := io.ReadAll(resp.Body)
	if err != nil {
		return nil, err
	}

	contentType := getFromHeaders(resp.Header, "Content-Type", "text/plain")
	server := getFromHeaders(resp.Header, "Server", "")

	return &Site{
		url:         rawUrl,
		domain:      domain,
		server:      server,
		protocol:    protocol,
		contentType: contentType,
		body:        string(bodyBytes),
		port:        port,
	}, nil
}

// Takes in a list of URL's and parses their content to Site's
func ParseURLs(urls []string) []*Site {
	result := make([]*Site, 0)
	for _, url := range urls {
		resp, err := scrapeSite(url)
		if err != nil {
			fmt.Printf("Error while processing %s: %v\n", url, err)
			continue
		}
		result = append(result, resp)
	}
	return result
}

//export parse_urls
func parse_urls(cUrls **C.char, count C.int) *C.Site {
	urlPtrs := (*[1 << 30]*C.char)(unsafe.Pointer(cUrls))[:count:count]
	type result struct {
		index int
		site  *Site
		err   error
	}
	results := make(chan result, count)

	for i := range int(count) {
		i := i // capture loop variable
		go func() {
			goUrl := C.GoString(urlPtrs[i])
			site, err := scrapeSite(goUrl)
			results <- result{index: i, site: site, err: err}
		}()
	}

	// Create a slice to hold Go-side results
	sitesData := make([]*Site, count)
	for range int(count) {
		r := <-results
		if r.err != nil {
			fmt.Printf("parse_urls(): Error scraping %d: %v\n", r.index, r.err)
			continue
		}
		sitesData[r.index] = r.site
	}

	// Allocate C array memory
	fmt.Printf("parse_urls():Allocating C memory\n")
	sites := (*C.Site)(C.malloc(C.size_t(count) * C.size_t(unsafe.Sizeof(C.Site{}))))

	for i, site := range sitesData {
		if site == nil {
			continue // skip failed site
		}
		fmt.Printf("parse_urls():Allocating memory for site: %v\n", site.url)
		cs := (*C.Site)(unsafe.Pointer(uintptr(unsafe.Pointer(sites)) + uintptr(i)*unsafe.Sizeof(C.Site{})))

		cs.url = C.CString(site.url)
		cs.domain = C.CString(site.domain)
		cs.server = C.CString(site.server)
		cs.protocol = C.CString(site.protocol)
		cs.contentType = C.CString(site.contentType)
		cs.body = C.CString(site.body)
		cs.port = C.int(site.port)
	}
	fmt.Printf("parse_urls():Returning site data\n\n")
	return sites
}

//export scrape_single_url
func scrape_single_url(cUrl *C.char) *C.Site {
	url := C.GoString(cUrl)      // Convert string back to Go string
	site, err := scrapeSite(url) // Get site data
	if err != nil {
		fmt.Printf("Error scraping %s: %v\n", url, err)
		return nil
	}
	// Convert site data back to C struct

	// Allocate memory for C struct
	cSite := (*C.Site)(C.malloc(C.size_t(unsafe.Sizeof(C.Site{}))))

	// Assign values
	cSite.url = C.CString(site.url)
	cSite.domain = C.CString(site.domain)
	cSite.server = C.CString(site.server)
	cSite.protocol = C.CString(site.protocol)
	cSite.contentType = C.CString(site.contentType)
	cSite.body = C.CString(site.body)
	cSite.port = C.int(site.port)

	return cSite
}

//export free_site
func free_site(site *C.Site) {
	if site == nil {
		return
	}
	C.free(unsafe.Pointer(site.url))
	C.free(unsafe.Pointer(site.domain))
	C.free(unsafe.Pointer(site.server))
	C.free(unsafe.Pointer(site.protocol))
	C.free(unsafe.Pointer(site.contentType))
	C.free(unsafe.Pointer(site.body))
	C.free(unsafe.Pointer(site))
}

//export free_sites
func free_sites(sites *C.Site, count C.int) {
	for i := range int(count) {
		sitePointer := (*C.Site)(unsafe.Pointer(uintptr(unsafe.Pointer(sites)) + uintptr(i)*unsafe.Sizeof(C.Site{})))

		C.free(unsafe.Pointer(sitePointer.url))
		C.free(unsafe.Pointer(sitePointer.domain))
		C.free(unsafe.Pointer(sitePointer.server))
		C.free(unsafe.Pointer(sitePointer.protocol))
		C.free(unsafe.Pointer(sitePointer.contentType))
		C.free(unsafe.Pointer(sitePointer.body))
	}
	C.free(unsafe.Pointer(sites))
}

func main() {}
