from multiprocessing import Process
import time
import random

def task(identifier: int):
    print(f"Started #{identifier} at {time.ctime()}")
    time.sleep(random.randint(0,10))
    print(f"Ended #{identifier} at {time.ctime()}")
    

if __name__ == '__main__':
    processes = []
    for index in range(10):
        process = Process(target=task, args=(index,))
        process.start()
        processes.append(process)

    for process in processes:
        process.join()