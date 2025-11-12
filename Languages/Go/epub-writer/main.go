package main

import (
	"archive/zip"
	"fmt"
	"io"
	"log"
	"os"
	"path"
	"path/filepath"
)

const fileToCreate = "mypub.epub"

func main() {
	newZipFile, err := os.Create("example.epub")
	if err != nil {
		log.Fatal(err)
		return
	}
	defer newZipFile.Close()
	zipWriter := zip.NewWriter(newZipFile)
	defer zipWriter.Close()
	data := `
		<h1>Hello my dudes</h1>
		<p>IT is me, the man</p>

	`
	createEpubData(zipWriter, data)
}

func addFileToZip(zipWriter *zip.Writer, filename string) {
	fileToZip, err := os.Open(filename)
	if err != nil {
		log.Println(err)
		return
	}
	defer fileToZip.Close()

	// Special rule for mimetype
	var w io.Writer
	if path.Base(filename) == "mimetype" {
		header := &zip.FileHeader{
			Name:   "mimetype",
			Method: zip.Store, // no compression
		}
		w, err = zipWriter.CreateHeader(header)
	} else {
		w, err = zipWriter.Create(filename)
	}

	if err != nil {
		log.Println(err)
		return
	}

	if _, err := io.Copy(w, fileToZip); err != nil {
		log.Println(err)
	}
}

func createEpubData(zipWriter *zip.Writer, htmlData string) {
	buildDir, err := os.MkdirTemp(".", "build")
	if err != nil {
		log.Fatal(err)
		return
	}
	defer os.Remove(buildDir)

	for _, folderName := range []string{"OEBPS", "META-INF"} {
		if err := os.Mkdir(path.Join(buildDir, folderName), 0770); err != nil {
			log.Fatal(err)
			return
		}
	}

	if err := CreateFileWithContent(path.Join(buildDir, "mimetype"), "application/epub+zip"); err != nil {
		log.Fatal(err)
		return
	}
	containerInfo := `<?xml version="1.0"?><container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container"><rootfiles><rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/></rootfiles></container>`
	contentFile := `<?xml version="1.0" encoding="utf-8"?>
<package version="3.0" xmlns="http://www.idpf.org/2007/opf" unique-identifier="bookid" xml:lang="en">
  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
    <dc:identifier id="bookid">urn:uuid:REPLACE-WITH-UUID</dc:identifier>
    <dc:title>Hello EPUB</dc:title>
    <dc:language>en</dc:language>
  </metadata>
  <manifest>
    <item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>
    <item id="hello" href="hello.xhtml" media-type="application/xhtml+xml"/>
  </manifest>
  <spine>
    <itemref idref="hello"/>
  </spine>
</package>`
	navFile := `<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">
  <head><title>Navigation</title></head>
  <body>
    <nav epub:type="toc" id="toc">
      <ol><li><a href="hello.xhtml">Hello</a></li></ol>
    </nav>
  </body>
</html>`
	helloPageData := fmt.Sprintf(`<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">
  <head><title>Hello</title></head>
  <body>
    %s
  </body>
</html>`, htmlData)

	if err := CreateFileWithContent(path.Join(buildDir, "META-INF", "container.xml"), containerInfo); err != nil {
		log.Fatal(err)
		return
	}
	if err := CreateFileWithContent(path.Join(buildDir, "OEBPS", "content.opf"), contentFile); err != nil {
		log.Fatal(err)
		return
	}
	if err := CreateFileWithContent(path.Join(buildDir, "OEBPS", "nav.xhtml"), navFile); err != nil {
		log.Fatal(err)
		return
	}
	if err := CreateFileWithContent(path.Join(buildDir, "OEBPS", "hello.xhtml"), helloPageData); err != nil {
		log.Fatal(err)
		return
	}

	addFileToZip(zipWriter, path.Join(buildDir, "mimetype"))
	addFolderToZip(zipWriter, buildDir, path.Join(buildDir, "OEBPS"))
	addFolderToZip(zipWriter, buildDir, path.Join(buildDir, "META-INF"))

}

func CreateFileWithContent(filepath, content string) error {
	if f, err := os.Create(filepath); err != nil {
		return err
	} else {
		_, err := f.WriteString(content)
		if err != nil {
			return err
		}
	}
	return nil
}

func addFolderToZip(zipWriter *zip.Writer, baseDir, folder string) {
	err := filepath.Walk(folder, func(filePath string, info os.FileInfo, err error) error {
		if err != nil {
			return err
		}

		if info.IsDir() {
			return nil
		}

		file, err := os.Open(filePath)
		if err != nil {
			return err
		}
		defer file.Close()

		// Relative path from the *base EPUB folder*, not just the subfolder
		relPath, err := filepath.Rel(baseDir, filePath)
		if err != nil {
			return err
		}

		// Ensure forward slashes for EPUB spec
		zipPath := filepath.ToSlash(relPath)

		w, err := zipWriter.Create(zipPath)
		if err != nil {
			return err
		}

		_, err = io.Copy(w, file)
		return err
	})

	if err != nil {
		log.Fatalf("Failed to add folder to zip: %v", err)
	}
}
