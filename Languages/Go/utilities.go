package main

import (
	"fmt"
	"os"
	"os/exec"
	"runtime"
)

// Allows you to build a binary out of a go project for all platforms
//
// # Parameters
//
// - name (string): The name to prefix the binaries with
// - binaryEntrypoint (string): The path to the entrypoint of the go project
//
// # Notes
//
// - The output format is `<name>-<GOOS>-<GOARCH><extension>`
//   - for example if name is "example" the output binaries would be all of the below:
//   - Mac OS: `example-darwin-arm64`, `example-darwin-amd64`
//   - Linux: `example-linux-arm64`, `example-linux-amd64`
//   - Windows: `example-windows-arm64.exe`, `example-windows-amd64.exe`
//
// - The binaryEntrypoint should be a full path (i.e. `/path/to/main.go` not `/path/to`)
//
// # Examples
//
//	// Please note import of the function is excluded
//	import(
//	  "fmt"
//	)
//
//	fmt.Println("Starting build")
//	buildall("example", "/path/to/main.go")
//	fmt.Println("Binaries finished building")
func BuildAll(name string, binaryEntrypoint string) {
	var command []string

	// Guarantee reset env variables after running
	defer func() {
		os.Setenv("GOOS", os.Getenv("GOHOSTOS"))
		os.Setenv("GOARCH", os.Getenv("GOHOSTARCH"))
	}()

	for _, currentOS := range []string{"linux", "darwin", "windows"} {
		for _, architecture := range []string{"amd64", "arm64"} {
			switch runtime.GOOS {
			case "windows":
				command = []string{"cmd", "/c"}
			default:
				command = []string{"bash"}
			}

			os.Setenv("GOOS", currentOS)
			os.Setenv("GOARCH", architecture)
			binaryExtension := ""
			if currentOS == "windows" {
				binaryExtension = ".exe"
			}

			filename := fmt.Sprintf("%s-%s-%s%s", name, currentOS, architecture, binaryExtension)
			command = append(command, "go", "build", "-o", filename, binaryEntrypoint)
			exec.Command(command[0], command[1:]...).Output()

		}
	}

	fmt.Println("Building releases for all platforms complete!")
}
