package main

import (
	"fmt"
	"math"
)

type SMOGResult struct {
	index float64
	level float64
}

func SimpleMeasureOfGobbledygook(text string) (*SMOGResult, error) {
	textInfo := GetTextData(text)
	if textInfo.sentences < 30 {
		return nil, fmt.Errorf("Cannot calculate SMOG result on text with less than 30 sentences")
	}

	return &SMOGResult{
		index: 3 + math.Sqrt(float64(textInfo.polySylabicWords)),
		level: (1.043 * math.Sqrt(float64(textInfo.polySylabicWords)*float64(30/textInfo.sentences))) + 3.1291,
	}, nil
}
