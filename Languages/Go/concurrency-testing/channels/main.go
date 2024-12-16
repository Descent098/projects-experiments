package main

import (
	"fmt"
	"math/rand"
	"sync"
)

func createLog(random *rand.Rand, logs chan string, messageNumber int) {
	logs <- fmt.Sprintf("Message #%d is %f", messageNumber, random.Float64())
}

func main() {
	random := rand.New(rand.NewSource(100))
	logs := make(chan string, 150)
	var waitGroup sync.WaitGroup

	for index := range 150 {
		waitGroup.Add(1)
		go func() {
			defer waitGroup.Done()
			createLog(random, logs, index+1)
		}()
	}

	waitGroup.Wait()
	close(logs)
	for log := range logs {
		fmt.Println(log)
	}

}
