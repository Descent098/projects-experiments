package main

import (
	"fmt"
	"sync"
)

type Counter struct {
	mutex sync.Mutex
	value int
}

func (counter *Counter) Increment() {
	counter.mutex.Lock()   // Lock the mutex to ensure exclusive access
	counter.value++        // Increment the counter
	counter.mutex.Unlock() // Unlock the mutex
}

func (counter *Counter) GetValue() int {
	counter.mutex.Lock()         // Lock the mutex to ensure safe read access
	defer counter.mutex.Unlock() // Unlock the mutex when the function returns
	return counter.value
}

func main() {
	counter := Counter{}
	var waitGroup sync.WaitGroup

	// Start 10 goroutines that increment the counter
	for index := 0; index < 10; index++ {
		waitGroup.Add(1)
		go func() {
			defer waitGroup.Done()
			for j := 0; j < 100; j++ {
				counter.Increment()
			}
		}()
	}

	// Wait for all goroutines to finish
	waitGroup.Wait()

	// Get the final value of the counter
	fmt.Println("Final Counter Value:", counter.GetValue())
}
