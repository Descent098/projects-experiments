package semaphore

import (
	"sync"
)

// Semaphore represents a counting semaphore that controls access to some shared resource (i.e. database)
type Semaphore struct {
	value     int        // The current value of the semaphore (blocks if < 1)
	mutex     sync.Mutex // A mutex to lock atomic operations
	condition *sync.Cond // A condition variable to wake-up threads without needing long-poling
}

// NewSemaphore creates a new semaphore with the given initial value acting as a count
//
// # Parameters
//
// initialValue (int): The initial count of the semaphore (essentially the capacity)
//
// # Returns
//
// *Semaphore: A pointer to the new semaphore instance
//
// # Examples
//
//	import (
//		"semaphore"
//	)
//
//	binary := NewSemaphore(1) // A binary semaphore
//
//	sem := NewSemaphore(10) // A counting semaphore with an initial capacity of 10
func NewSemaphore(initialValue int) *Semaphore {
	sem := &Semaphore{
		value: initialValue,
	}
	sem.condition = sync.NewCond(&sem.mutex)
	return sem
}

// Wait decrements the semaphore value, blocking if it would go below zero
func (s *Semaphore) Wait() {
	s.mutex.Lock()
	defer s.mutex.Unlock()

	// Block while semaphore value is 0 or negative
	for s.value <= 0 {
		s.condition.Wait()
	}
	s.value-- // Decrement semaphore value under mutex protection
}

// Signal increments the semaphore value and wakes one waiting goroutine
func (s *Semaphore) Signal() {
	s.mutex.Lock()
	defer s.mutex.Unlock()

	s.value++            // Increment semaphore value under mutex protection
	s.condition.Signal() // Wake up one waiting goroutine
}
