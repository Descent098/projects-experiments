package main

import (
	"fmt"

	"github.com/c-bata/go-prompt"
)

func completer(d prompt.Document) []prompt.Suggest {
	s := []prompt.Suggest{
		{Text: "ALL", Description: "All environments"},
		{Text: "ALL STAGING", Description: "All staging environments"},
		{Text: "ALL PROD", Description: "All production environments"},
		{Text: "SELECT SPECIFIC", Description: "Select a specific environment"},
	}
	return prompt.FilterHasPrefix(s, d.GetWordBeforeCursor(), true)
}

func main() {
	fmt.Println("Please select table.")
	t := prompt.Input("> ", completer)
	fmt.Println("You selected " + t)
}
