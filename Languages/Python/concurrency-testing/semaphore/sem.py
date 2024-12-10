import threading

class Semaphore:
    """
    Semaphore represents a counting semaphore that controls access
    to a shared resource.
    """
    def __init__(self, initial_value:int):
        """Initialize the semaphore with the given initial value.

        Parameters
        ----------
        initial_value : int
            The initial value of the semaphore (essentially the capacity)
        """
        self.value = initial_value
        self.mutex = threading.Lock()
        self.condition = threading.Condition(self.mutex)

    def wait(self):
        """
        Decrement the semaphore value, blocking if it would go below zero.
        """
        with self.condition:
            while self.value <= 0:
                self.condition.wait()
            self.value -= 1  # Decrement semaphore value under mutex protection

    def signal(self):
        """
        Increment the semaphore value and wake one waiting thread.
        """
        with self.condition:
            self.value += 1  # Increment semaphore value under mutex protection
            self.condition.notify()  # Wake up one waiting thread

if __name__ == "__main__":
    # Code to test with
    import time
    def worker(semaphore, id):
        print(f"Worker {id} waiting...")
        semaphore.wait()
        print(f"Worker {id} working...")
        time.sleep(1)
        print(f"Worker {id} done.")
        semaphore.signal()

    sem = Semaphore(2)  # Semaphore with an initial value of 2

    threads = [threading.Thread(target=worker, args=(sem, i)) for i in range(50)]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()