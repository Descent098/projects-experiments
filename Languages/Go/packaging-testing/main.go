package main

import (
	"fmt"

	"github.com/Descent098/speyl"
)

func main() {
	validWords := []string{"hi", "hello", "bonjour", "alumni"}

	inputWord := "alumni"
	s := speyl.SuggestWord(inputWord, validWords) // Returns algorithms.Suggestion{Likelihood: 1.0, Word: "alumni"}
	// Prints: alumni is alumni with %100.00 Likelihood
	fmt.Printf("%s is %s with %%%.2f Likelihood\n", inputWord, s.Word, s.Likelihood*100)

	misspeltWord := "almni"
	s = speyl.SuggestWord(misspeltWord, validWords) // Returns algorithms.Suggestion{Likelihood: 0.944, Word: "alumni"}
	// Prints: almni is alumni with %94.44 Likelihood
	fmt.Printf("%s is %s with %%%.2f Likelihood\n", misspeltWord, s.Word, s.Likelihood*100)
}
