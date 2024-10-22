package main

import (
	"fmt"
	"runtime"
)

func printMemStats() {
	var m runtime.MemStats   // Create empty struct
	runtime.ReadMemStats(&m) // Populate struct with data

	fmt.Printf("Alloc = %v Mb\n", bToMb(m.Alloc))            // Total Heap objects allocation size
	fmt.Printf("Total Alloc = %v Mb\n", bToMb(m.TotalAlloc)) // Total memory EVER allocated by program (only goes up over time)

	fmt.Printf("Sys = %v Mb\n", bToMb(m.Sys)) // All memory program has attained, includes reserved but unused memory
}

func bToMb(b uint64) uint64 {
	// Converts Bytes to megaBtyes
	return b / 1000 / 1000
}

func main() {
	fmt.Println("Mem stats before:")
	printMemStats()

	s := make([]int, 10_000_000)

	for i := range s {
		s[i] = i
	}

	fmt.Println("Mem Stats after:")
	printMemStats()

}
