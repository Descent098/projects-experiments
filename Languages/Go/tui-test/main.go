package main

import (
	"fmt"

	"github.com/charmbracelet/huh"
)

func main() {
	environments := ""
	huh.NewSelect[string]().
		Title("Pick a country.").
		Options(
			huh.NewOption("ALL", "ALL"),
			huh.NewOption("ALL STAGING", "ALL STAGING"),
			huh.NewOption("ALL PROD", "ALL PROD"),
			huh.NewOption("SELECT SPECIFIC", "SELECT SPECIFIC"),
		).
		Value(&environments).Run()

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
	selectedSites := []string{}

	environments := []string{"active-living", "alumni", "ancillary", "arts", "campaign-301", "campaign-401", "charbonneau", "cirl", "cumming", "esl", "explore", "finance", "grad", "haskayne", "hbi", "homepage", "hr", "hunter-hub", "imc", "it", "kinesiology", "law", "libin", "mccaig", "news", "nursing", "obrieniph", "outdoor-centre", "oval", "provost", "qatar", "research", "research4kids", "risk", "sapl", "schulich", "science", "secretariat", "snyder", "socialwork", "sport-med", "taylor-institute", "ucalgary", "vet", "web", "werklund", "news", "profiles", "homepage"}

	var opts []huh.Option[string]
	for _, env := range environments {
		opts = append(opts, huh.NewOption(env, env))
	}
	huh.NewMultiSelect[string]().
		Title("Which environment:").
		Options(
			opts...,
		).
		Value(&selectedSites).Run()
	return selectedSites
}
