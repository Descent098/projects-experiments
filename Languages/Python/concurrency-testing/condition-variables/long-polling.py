import threading
import time

# Shared data
data = []
mutex = threading.Lock()  # Lock to protect shared data

# Producer function
def producer():
    global data
    for i in range(5):  # Produce 5 items
        with mutex:
            print(f"Producer: Adding item {i}")
            data.append(i)  # Produce an item
        time.sleep(1)  # Simulate time taken to produce

# Consumer function
def consumer():
    global data
    for _ in range(5):  # Consume 5 items
        while True:
            with mutex:
                if data:  # Check if there's data to consume
                    item = data.pop(0)
                    print(f"Consumer: Consumed item {item}")
                    break
            time.sleep(0.1)  # Wait before checking again (long-polling delay)

# Create and start the threads
producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

producer_thread.start()
consumer_thread.start()

# Wait for both threads to complete
producer_thread.join()
consumer_thread.join()

print("All items have been produced and consumed.")
