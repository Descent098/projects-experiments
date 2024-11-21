package main

import (
	"fmt"

	"github.com/AlecAivazis/survey/v2"
)

func main() {

	whichEnv := &survey.Select{
		Message: "Which environment:",
		Options: []string{"ALL", "ALL STAGING", "ALL PROD", "SELECT SPECIFIC"},
	}
	environments := ""
	survey.AskOne(whichEnv, &environments)

	var selectedSites []string

	if environments == "SELECT SPECIFIC" {
		selectedSites = selectSite()
	} else {
		switch environments {
		case "ALL":
			selectedSites = []string{"all"}
		case "ALL STAGING":
			selectedSites = []string{"all staging"}
		case "ALL PROD":
			selectedSites = []string{"all prod"}
		}
	}

	fmt.Printf("Environments selected:\n\t%v\nSite Selected:\n\t%v", environments, selectedSites)

}

func selectSite() []string {
	sites := []string{"alumni", "social-work", "werklund"}
	selectedSites := []string{}

	whichSite := &survey.MultiSelect{
		Message: "Which environment:",
		Options: sites,
	}

	survey.AskOne(whichSite, &selectedSites)
	return selectedSites
}
