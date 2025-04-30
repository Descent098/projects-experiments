package main

/*
#include <stdlib.h>
*/
import "C"
import (
	"fmt"
)

// Add the following commented code, indicating that after export, it can be called by Python
// Note that the following comment should not be written as "// export xxx", but as "//export xxx"
// Otherwise, it cannot be called

//export Greeting
func Greeting() {
	fmt.Println("Hello from Go!")
}

//export GreetS
func GreetS(name *C.char) *C.char {
	goName := C.GoString(name)
	result := fmt.Sprintf("HELLO %s", goName)
	return C.CString(result) // Return a C-compatible string
}

func main() {
	// Do nothing
}
