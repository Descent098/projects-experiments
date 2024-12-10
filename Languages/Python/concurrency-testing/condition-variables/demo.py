import threading
import time

# Shared data
data = []
condition = threading.Condition()

# Producer function
def producer():
    global data
    for i in range(5):  # Produce 5 items
        with condition:
            print(f"Producer: Adding item {i}")
            data.append(i)  # Produce an item
            condition.notify()  # Notify the consumer
        time.sleep(1)  # Simulate time taken to produce

# Consumer function
def consumer():
    global data
    for _ in range(5):  # Consume 5 items
        with condition:
            while not data:  # Wait until there is data
                condition.wait()
            item = data.pop(0)  # Consume the item
            print(f"Consumer: Consumed item {item}")

# Create and start the threads
producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

producer_thread.start()
consumer_thread.start()

# Wait for both threads to complete
producer_thread.join()
consumer_thread.join()

print("All items have been produced and consumed.")
