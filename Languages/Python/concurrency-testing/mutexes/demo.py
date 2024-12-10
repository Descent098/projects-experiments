import threading

# Shared resource
counter = 0

# Create a lock
mutex = threading.Lock()

def increment_counter():
    global counter
    for _ in range(1000):
        # Entry Section
        mutex.acquire() # Acquire the lock before modifying the shared resource
        try:
            # Critical Section
            counter += 1
        finally:
            # Exit section
            mutex.release() # Release the lock

# Create multiple threads
threads = []
for _ in range(5):  # 5 threads
    t = threading.Thread(target=increment_counter)
    threads.append(t)
    t.start()

# Wait for all threads to complete
for t in threads:
    t.join()

print(f"Final counter value: {counter}")
