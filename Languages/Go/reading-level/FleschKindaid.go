package main

type FleschKincaidResult struct {
	ease  float32
	level float32
}

// Calculates the Flesch Kindcade information of text
//
// # Parameters
//   - text(string): The text to analyze
//
// # Returns
//   - FleschKincaidResult: the analytics of the text
//
// # Notes
//  - Accuracy is limited by syllable estimation and sentence count estimation
// 	- Typically this function will UNDERESTIMATE difficulty (lower level, higher ease)
//
// # Reference
//  - https://en.wikipedia.org/wiki/Flesch%E2%80%93Kincaid_readability_tests
//  - https://github.com/mholtzscher/syllapy Syllable Heuristic
func FleschKincaid(text string) FleschKincaidResult {
	textInfo := GetTextData(text)

	return FleschKincaidResult{
		ease:  206.835 - (1.015 * (textInfo.words / textInfo.sentences)) - (84.6 * (textInfo.syllables / textInfo.words)),
		level: 0.39*(textInfo.words/textInfo.sentences) + 11.8*(textInfo.syllables/textInfo.words) - 15.59,
	}

}
