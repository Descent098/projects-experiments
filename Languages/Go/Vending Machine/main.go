package main

import (
	"fmt"
	"os"

	// Third party packages
	"github.com/olekukonko/tablewriter"
)

// TODO: Move vending machine struct and methods to a separate package
// A Struct representing a vending machine including how much credit is in the machine, what products, and what coins are available
type vendingMachine struct {
	credit   int           // The amount that is able to be spent on products
	products [6][4]product // 6 Rows of 4 products
	coins    []coin        // what coins are available to the machine TODO: Allow to keep track of how many of each later
}

// A Struct to represent generic products like cans of pop, candy bars etc
type product struct {
	cost  int    // how much it costs (in cents) i.e. CAD$2.25 would be 225
	name  string // The product name i.e. coca-cola
	count int    // The amount of a product left
}

// TODO: Look at implementing a currency localization as part of the struct
// A Struct to represent coins in various currencies
type coin struct {
	value int    // How much the coin is worth
	name  string // The colloquial name of the coin
}

// Currency is a dummy type for the enumerator found below
type Currency int

// An enumerator of all the various currencies supported
const (
	CAD Currency = iota
	USD Currency = iota
)

//addCoins takes a string indicating a currency name and returns a slice of coins with the coin values of that currency
func addCoins(currency Currency) []coin {
	var coins []coin

	// TODO: Implement more currencies
	switch currency { // This switch statement determines the coins to add based on selected currency
	case 0: // Add CAD coins
		toonie := coin{value: 200, name: "Toonie"}
		loonie := coin{value: 100, name: "Loonie"}
		quarter := coin{value: 25, name: "Quarter"}
		dime := coin{value: 10, name: "Dime"}
		nickle := coin{value: 5, name: "Nickle"}
		coins = append(coins, toonie, loonie, quarter, dime, nickle)

	case 1: // Add USD coins
		quarter := coin{value: 25, name: "Quarter"}
		dime := coin{value: 10, name: "Dime"}
		nickle := coin{value: 5, name: "Nickle"}
		penny := coin{value: 1, name: "Penny"}
		coins = append(coins, quarter, dime, nickle, penny)

	}
	return coins
}

// Takes vending machine contents and prints a human-readable representation of available products
func printMachineContents(machine vendingMachine) {
	table := tablewriter.NewWriter(os.Stdout)

	var rowContent []string

	// Setting table formatting
	table.SetHeader([]string{"Row Number", "Column 1", "Column 2", "Column 3", "Column 4"})
	table.SetFooter([]string{"", "", "", "Available Credit: ", fmt.Sprintf("%v", machine.credit)})

	// Iterating through current vending machine contents and adding them to the table
	for currentRow := 0; currentRow < 6; currentRow++ { // Each row
		rowContent = nil                                                     // resetting the slice after each iteration
		rowContent = append(rowContent, fmt.Sprintf("Row %v", currentRow+1)) // Add current row number
		for currentProduct := 0; currentProduct < 4; currentProduct++ {      // Each Product line
			rowContent = append(rowContent, fmt.Sprintf("%v x%v", machine.products[currentRow][currentProduct].name, machine.products[currentRow][currentProduct].count))
		}
		table.Append(rowContent)

	}
	fmt.Printf("\n\n") // Adding spacing before rendering the table
	table.Render()
}

// Takes vending machine as argument and decrements the selected products count, and decrements machines remaining credit
func buyProduct(machine vendingMachine, selection [2]int) vendingMachine {

	// Aliasing selection for better readability
	selectedProduct := machine.products[selection[0]][selection[1]]

	// fmt.Printf("\n\nAttempting to purchase %v for %v with %v credit", selectedProduct.name, selectedProduct.cost, machine.credit)
	if selectedProduct.cost <= machine.credit { // if you have enough credit to buy
		// decrement the products' count by 1
		fmt.Printf("\nPurchasing %v for %v with %v credit", selectedProduct.name, selectedProduct.cost, machine.credit)
		selectedProduct.count = selectedProduct.count - 1

		// Decrement remaining credit by product cost
		machine.credit -= selectedProduct.cost

	} else { // If you don't have enough credit to buy the item
		fmt.Printf("\nSorry you're broke my dude")
	}
	return machine

}

func main() {
	/* TODO:
	- Add user input for:
		- selecting which currency to use
	- Look at a way to serialize the stock of the vending machine
	- Pretty print the change given back after purchase
	- Keep track of how much change (in terms of each coin) is actually available to the machine
	*/

	// instantiating products list for vending machine construction later
	var products [6][4]product

	// Dummy product for testing
	coke := product{cost: 225, name: "Coca-Cola", count: 5}

	// Fill vending machine
	for currentRow := 0; currentRow < 6; currentRow++ { // Each row
		for currentProduct := 0; currentProduct < 4; currentProduct++ { // Each product
			products[currentRow][currentProduct] = coke // Fill each with coke
		}
	}

	coins := addCoins(CAD)              // Get the coins for localized currency
	for _, currentCoin := range coins { // For loop to print coin information for testing purposes
		fmt.Printf("Coin name: %v \nCoin Value (in cents): %v\n", currentCoin.name, currentCoin.value)
	}

	fmt.Println("How much credit are you putting in? (in cents; i.e. CAD$2.25 is 225): ")
	var credit int
	fmt.Scan(&credit)

	// Instantiate the vending machine with the established values
	machine := vendingMachine{credit, products, coins}

	// Getting selection from user
	var selection [2]int

	// TODO: Move to vending machine package
	for { // infinite loop
		// Print vending machine contents at start of each iteration
		printMachineContents(machine)

		// Row Selection
		fmt.Print("\n\nwhich row?: ")
		var selectedRow int
		fmt.Scan(&selectedRow)
		selection[0] = selectedRow - 1

		// Column Selection
		fmt.Print("which Column?: ")
		var selectedColumn int
		fmt.Scan(&selectedColumn)
		selection[1] = selectedColumn - 1

		machine = buyProduct(machine, selection)

	}

}
