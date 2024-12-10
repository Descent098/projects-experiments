package semaphore

import (
	"sync"
	"testing"
	"time"
)

func TestSemaphoreBasic(testingState *testing.T) {
	semaphore := NewSemaphore(2)

	// Test initial value
	if semaphore.value != 2 {
		testingState.Errorf("Expected 2, got %d", semaphore.value)
	}
}

func TestSemaphoreConcurrent(testingState *testing.T) {
	// Setup the initial variables to run the test
	const (
		numGoroutines = 100
		initialValue  = 3
		timeout       = 5 * time.Second
	)

	semaphore := NewSemaphore(initialValue)
	var waitGroup sync.WaitGroup

	// Counter to track concurrent access
	activeGoroutines := 0
	var counterMutex sync.Mutex

	// Channel to report errors from goroutines
	errorChan := make(chan string, numGoroutines)

	// Start time for timeout checking
	start := time.Now()

	// Launch multiple goroutines that will compete for the semaphore
	for index := 0; index < numGoroutines; index++ {
		waitGroup.Add(1)
		go func(id int) {
			defer waitGroup.Done()

			// Acquire semaphore
			semaphore.Wait()

			// Track number of active goroutines
			counterMutex.Lock()
			activeGoroutines++
			current := activeGoroutines
			counterMutex.Unlock()

			// Verify that we never exceed the semaphore's capacity
			if current > initialValue {
				errorChan <- "Too many goroutines"
			}

			// Simulate some work
			time.Sleep(10 * time.Millisecond)

			// Decrease active count
			counterMutex.Lock()
			activeGoroutines--
			counterMutex.Unlock()

			// Release semaphore
			semaphore.Signal()

			// Check for timeout
			if time.Since(start) > timeout {
				errorChan <- "Test took too long probable deadlock"
			}
		}(index)
	}

	// Wait for all goroutines to complete or timeout
	// functionally the same as `pthred_join()` in C
	done := make(chan struct{})
	go func() {
		waitGroup.Wait()
		close(done)
	}()

	select {
	case <-done:
		// Test completed successfully
	case err := <-errorChan:
		testingState.Errorf("Test failed: %s", err)
	case <-time.After(timeout):
		testingState.Errorf("Test timed out after %v", timeout)
	}
}

func TestSemaphoreStress(testingState *testing.T) {
	const (
		initialValue = 5
		iterations   = 1000
	)

	semaphore := NewSemaphore(initialValue)
	var waitGroup sync.WaitGroup

	// Launch producer goroutines that signal
	for index := 0; index < iterations; index++ {
		waitGroup.Add(1)
		go func() {
			defer waitGroup.Done()
			semaphore.Signal()
		}()
	}

	// Launch consumer goroutines that wait
	for index := 0; index < iterations; index++ {
		waitGroup.Add(1)
		go func() {
			defer waitGroup.Done()
			semaphore.Wait()
		}()
	}

	// Wait for all goroutines to complete
	waitGroup.Wait()

	// Verify final value matches initial value
	if semaphore.value != initialValue {
		testingState.Errorf("Expected value %d, got %d", initialValue, semaphore.value)
	}
}
