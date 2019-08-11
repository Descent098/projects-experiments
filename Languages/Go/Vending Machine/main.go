package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"

	"github.com/olekukonko/tablewriter"
)

// TODO: Move vending machine struct and methods to a separate package
// A Struct representing a vending machine including how much credit is in the machine, what products, and what coins are available
type vendingMachine struct {
	credit   int              // The amount that is able to be spent on products
	products [6][4][5]product // 6 Rows of 4 product lines, with a maximum of 5 of that product in the line in stock
	coins    []coin           // what coins are available to the machine TODO: Allow to keep track of how many of each later
}

// A Struct to represent generic products like cans of pop, candy bars etc
type product struct {
	cost int
	name string
}

// TODO: Look at implementing a currency localization as part of the struct
// A Struct to represent coins in various currencies
type coin struct {
	value int
	name  string
}

//addCoins takes a string indicating a currency name and returns a slice of coins with the coin values of that currency
func addCoins(currency string) []coin {
	var coins []coin

	// TODO: Implement more currencies
	if strings.Contains(currency, "CAD") { // Add CAD coins
		toonie := coin{value: 200, name: "Toonie"}
		loonie := coin{value: 100, name: "Loonie"}
		quarter := coin{value: 25, name: "Quarter"}
		dime := coin{value: 10, name: "Dime"}
		nickle := coin{value: 5, name: "Nickle"}
		coins = append(coins, toonie, loonie, quarter, dime, nickle)
	}

	if strings.Contains(currency, "USD") { // Add USD coins
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

	table.SetHeader([]string{"Row Number", "Column 1", "Column 2", "Column 3", "Column 4"})
	for currentRow := 0; currentRow < 6; currentRow++ { // Each row
		rowContent = nil
		rowContent = append(rowContent, fmt.Sprintf("Row %v", currentRow+1)) // Add current row number
		for productLine := 0; productLine < 4; productLine++ {               // Each Product line
			rowContent = append(rowContent, fmt.Sprintf("%v", machine.products[currentRow][productLine][2].name))
		}
		table.Append(rowContent)

	}
	table.Render()
}

func main() {
	/* TODO:
	- Add user input for:
		- selecting which currency to use
		- Inputting credit to the vending machine
		- Making a product selection
	- Be able to 'purchase' products
	- Get change back after purchasing products
	- Look at a way to serialize the stock of the vending machine
	- Pretty print the change given back after purchase
	- Keep track of how much change is actually available to the machine
	*/

	reader := bufio.NewReader(os.Stdin)

	// instantiating products list for vending machine construction later
	var products [6][4][5]product

	// Dummy product for testing
	coke := product{cost: 225, name: "Coca-Cola"}

	// Fill vending machine
	for currentRow := 0; currentRow < 6; currentRow++ { // Each row
		for productLine := 0; productLine < 4; productLine++ { // Each Product line
			for currentProduct := 0; currentProduct < 5; currentProduct++ { // Each product
				products[currentRow][productLine][currentProduct] = coke // Fill each with coke
			}
		}
	}

	coins := addCoins("CAD")            // Get the coins for localized currency
	for _, currentCoin := range coins { // For loop to print coin information for testing purposes
		fmt.Printf("Coin name: %v \nCoin Value (in cents): %v\n", currentCoin.name, currentCoin.value)
	}

	// Create the vending machine with the established values
	machine := vendingMachine{245, products, coins}

	// Pretty printing machine info
	fmt.Printf("\n\nMachine Credit: %v \nMachine Products: \n", machine.credit)
	printMachineContents(machine)
	fmt.Printf("\nMachine Coins: %v", machine.coins)

	// User input testing
	fmt.Print("\n\nWhat do you want to buy?: ")
	text, _ := reader.ReadString('\n')
	fmt.Println("selection made: " + text)
}
