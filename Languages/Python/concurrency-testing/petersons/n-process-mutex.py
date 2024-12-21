from threading import Lock
from concurrent.futures import ThreadPoolExecutor

n = 12  # Number of processes (threads)
flag = [False] * n  # Flags for each process
turn = [-1] * (n - 1)  # Turn array for Peterson's n-process hierarchy
counter = 0  # Shared counter
mutex = Lock()

def critical_section(process_id: int):
    """Critical section logic."""
    global counter
    print(f"In the critical section for {process_id}, and counter is {counter}")
    c = counter
    c += 100
    counter = c
    print(f"Exiting the critical section for {process_id}, and counter is {counter}")

def run_thread(process_id: int):
    """Thread function to execute the Peterson's algorithm."""
    print(f"Starting thread {process_id}, and counter is {counter}")
    completed = 0
    TIMES_TO_RUN_CRITICAL_SECTION = 10

    while completed < TIMES_TO_RUN_CRITICAL_SECTION:
        with mutex:
            critical_section(process_id)
        completed += 1
    print(f"Exiting petersons() in thread {process_id}, and counter is {counter}")
    

if __name__ == "__main__":
    import time
    t1 = time.time()
    with ThreadPoolExecutor(max_workers=n) as executor:
        for i in range(n):
            executor.submit(run_thread, i)
    t2 = time.time()
    
    print(f"Took {t2-t1} seconds")
    print(f"Which is {(t2-t1)/60} mins")