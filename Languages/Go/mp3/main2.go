package main

import (
	"bytes"
	"encoding/base64"
	"fmt"
	"image"
	"image/jpeg"
	"image/png"
	"mp3/core"
	"os"

	"github.com/dhowden/tag"
	"golang.org/x/image/draw"
)

// imageResize resizes the given image bytes to the specified width and height
// (only if larger than those dimensions).
func imageResize(imgData []byte, mimeType core.MIMEType, targetWidth, targetHeight int) ([]byte, error) {
	img, format, err := image.Decode(bytes.NewReader(imgData))
	if err != nil {
		return nil, fmt.Errorf("failed to decode image: %v", err)
	}

	bounds := img.Bounds()
	width := bounds.Dx()
	height := bounds.Dy()

	// Only resize if the image is larger than target size
	if width <= targetWidth && height <= targetHeight {
		return imgData, nil
	}

	// Create a new RGBA image for the resized result
	resized := image.NewRGBA(image.Rect(0, 0, targetWidth, targetHeight))
	draw.CatmullRom.Scale(resized, resized.Bounds(), img, bounds, draw.Over, nil)

	// Encode back to bytes
	var buf bytes.Buffer
	switch format {
	case "jpeg":
		err = jpeg.Encode(&buf, resized, &jpeg.Options{Quality: 90})
	case "png":
		err = png.Encode(&buf, resized)
	default:
		// Fallback based on MIME type
		switch mimeType {
		case "image/jpeg":
			err = jpeg.Encode(&buf, resized, &jpeg.Options{Quality: 90})
		case "image/png":
			err = png.Encode(&buf, resized)
		default:
			return nil, fmt.Errorf("unsupported image format: %s", format)
		}
	}
	if err != nil {
		return nil, fmt.Errorf("failed to encode resized image: %v", err)
	}

	return buf.Bytes(), nil
}

// base64EncodeImage encodes image bytes to a Base64 data URI string.
func base64EncodeImage(imgData []byte, mimeType core.MIMEType) string {
	base64Data := base64.StdEncoding.EncodeToString(imgData)
	return fmt.Sprintf("data:%s;base64,%s", mimeType, base64Data)
}

func main() {
	f, err := os.Open("I'll Tell Me Ma-Sinead O Connor.mp3")
	if err != nil {
		panic(err)
	}
	defer f.Close()

	m, err := tag.ReadFrom(f)
	if err != nil {
		panic(err)
	}

	fmt.Println("Title:", m.Title())
	fmt.Println("Artist:", m.Artist())
	fmt.Println("Album Artist:", m.AlbumArtist())
	fmt.Println("Album:", m.Album())
	fmt.Println("Year:", m.Year())
	trackNumber, totalTracks := m.Track()
	fmt.Println("Track:", trackNumber, "/", totalTracks)

	// Get attached picture
	pic := m.Picture()
	if pic == nil {
		fmt.Println("No picture found in metadata.")
		return
	}

	fmt.Println("Picture MIME Type:", pic.MIMEType)
	fmt.Println("Picture Description:", pic.Description)
	fmt.Printf("Picture Size: %d bytes\n", len(pic.Data))

	// Resize the image if needed
	resizedData, err := imageResize(pic.Data, pic.MIMEType, 300, 300)
	if err != nil {
		panic(err)
	}

	// Base64 encode the image
	base64Str := base64EncodeImage(resizedData, pic.MIMEType)

	// Write to file
	err = os.WriteFile("metadata.txt", []byte(base64Str), 0644)
	if err != nil {
		panic(err)
	}

	fmt.Println("✅ Base64 metadata written to metadata.txt")
}
