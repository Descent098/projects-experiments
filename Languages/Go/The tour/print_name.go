package main

// Import statements:
// fmt; Used to format and print to stdout
// math/rand; used to generate random numbers
import (
	"fmt"
	"bufio"
	"os"
)

// The main function of the package; What gets run after compilation
func main() {
	//reading a string
    reader := bufio.NewReader(os.Stdin)
    var name string
    fmt.Println("What is your name?")
	name, _ = reader.ReadString('\n')
	print_name(name)
	
}

func print_name(name string){
	fmt.Println("Hello " + name + "!") 
}