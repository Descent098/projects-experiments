package generators

import (
	"fmt"
	"os"
)

// File contains functions for generating test files

// TODO: remove
func DRAWHEHE(width, height, thickness int) {
	img := make([][]int, height)
	for y := range img {
		img[y] = make([]int, width)
	}

	fillRect := func(img [][]int, x, y, w, h int) {
		for row := y; row < y+h; row++ {
			for col := x; col < x+w; col++ {
				// bounds safety
				if row >= 0 && row < len(img) &&
					col >= 0 && col < len(img[0]) {
					img[row][col] = 1
				}
			}
		}
	}

	println("height is", len(img), "width is", len(img[0]))

	drawH := func(x, y int) {
		height := 60
		width := 30

		// left vertical
		fillRect(img, x, y, thickness, height)

		// right vertical
		fillRect(img, x+width, y, thickness, height)

		// middle bar
		fillRect(img, x, y+(height/2)-(thickness/2), width+thickness, thickness)
	}

	drawE := func(x, y int) {
		height := 60
		width := 30

		// left vertical
		fillRect(img, x, y, thickness, height)

		// top
		fillRect(img, x, y, width, thickness)

		// middle
		fillRect(img, x, y+(height/2)-(thickness/2), width, thickness)

		// bottom
		fillRect(img, x, y+height-thickness, width, thickness)
	}

	drawH(40, 14)
	drawE(100, 14)
	drawH(150, 14)
	drawE(210, 14)

	f, err := os.Create("hehe.pbm")
	if err != nil {
		panic(err)
	}
	defer f.Close()

	fmt.Fprintf(f, "P1\n")
	fmt.Fprintf(f, "%d %d\n", width, height)

	for y := range height {
		for x := range width {
			fmt.Fprintf(f, "%d ", img[y][x])
		}
		fmt.Fprintln(f)
	}
}
