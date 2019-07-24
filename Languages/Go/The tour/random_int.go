package main

// Import statements:
// fmt; Used to format and print to stdout
// math/rand; used to generate random numbers
import (
	"fmt"
	"math/rand"
)

// The main function of the package; What gets run after compilation
func main() {
	// This call will always produce the same number because it's deterministic
	fmt.Println("My favorite number is", rand.Intn(10)) 
}
