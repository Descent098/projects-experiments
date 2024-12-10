import time
import random
import concurrent.futures

def task(identifier:int):
    print(f"inside task() #{identifier}")
    time.sleep(random.randint(0,10))
    print(f"done task() #{identifier}")

with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
    for index in range(20):
        pool.submit(task, index)