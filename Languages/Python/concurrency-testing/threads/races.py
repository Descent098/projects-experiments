import time
import random
import threading

def increment():
    with open("counter.txt") as c:
        counter = int(c.read())
        print(f"Opened with count = {counter}")
    time.sleep(random.random())
    for _ in range(1000000):
        counter += 1
    with open("counter.txt", "w+") as c:
        c.write(str(counter))
    print(f"Closed with count = {counter}")
    
threads = []
    
for _ in range(15):
    t = threading.Thread(target=increment)
    t.start()
    threads.append(t)

for t in threads:
    t.join()

