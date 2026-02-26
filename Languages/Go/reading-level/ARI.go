package main

import "math"

func AutomatedReadabilityIndex(text string) int {
	textInfo := GetTextData(text)

	return int(math.Ceil(float64(4.71*(textInfo.characters/textInfo.words) + 0.5*(textInfo.words/textInfo.sentences) - 21.43)))

}
