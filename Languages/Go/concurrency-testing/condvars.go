// A quick and dirty demo of condition variables
package main

import (
	"fmt"
	"sync"
	"time"
)

type Queue struct {
	data      []int
	mutex     sync.Mutex
	condition *sync.Cond
}

func NewQueue() *Queue {
	q := &Queue{}
	q.condition = sync.NewCond(&q.mutex)
	return q
}

// Enqueue adds an item to the queue and notifies waiting consumers
func (queue *Queue) Enqueue(item int) {
	queue.mutex.Lock()
	queue.data = append(queue.data, item)
	fmt.Println("Produced:", item)
	queue.condition.Signal() // Notify one waiting consumer
	queue.mutex.Unlock()
}

// Dequeue removes an item from the queue, waiting if necessary
func (queue *Queue) Dequeue() int {
	queue.mutex.Lock()
	for len(queue.data) == 0 {
		queue.condition.Wait() // Wait until an item is available
	}
	item := queue.data[0]
	queue.data = queue.data[1:]
	queue.mutex.Unlock()
	fmt.Println("Consumed:", item)
	return item
}

func main() {
	queue := NewQueue()
	var waitGroup sync.WaitGroup

	// Consumer (notice it goes first and waits nicely)
	waitGroup.Add(1)
	go func() {
		defer waitGroup.Done()
		for index := 1; index <= 10; index++ {
			queue.Dequeue()
			time.Sleep(1 * time.Second) // Simulate consumption delay
		}
	}()

	// Producer
	waitGroup.Add(1)
	go func() {
		defer waitGroup.Done()
		for index := 1; index <= 10; index++ {
			time.Sleep(500 * time.Millisecond) // Simulate production delay
			queue.Enqueue(index)
		}
	}()

	// Wait for both producer and consumer to finish
	waitGroup.Wait()
	fmt.Println("All tasks completed.")
}
