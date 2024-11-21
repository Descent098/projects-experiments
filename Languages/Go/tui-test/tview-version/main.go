package tviewversion

import "github.com/rivo/tview"

func main() {

	form := tview.NewForm().AddDropDown(
		"Select an option (hit Enter): ",
		[]string{"ALL", "ALL STAGING", "ALL PROD", "SELECT SPECIFIC"},
		1, func(option string, optionIndex int) {
			switch option {
			case "ALL":
				println("GOT ALL")
			case "ALL STAGING":
				println("GOT ALL STAGING")
			case "ALL PROD":
				println("GOT ALL PROD")
			case "SELECT SPECIFIC":
				println("GOT SELECT SPECIFIC")
			default:
				break
			}

		},
	)
	if err := tview.NewApplication().SetRoot(form, true).Run(); err != nil {
		panic(err)
	}
}
