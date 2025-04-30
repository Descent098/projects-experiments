import time
from concurrent.futures import ThreadPoolExecutor

# Number of processes
number_of_processes = 30
TIMES_TO_RUN_CRITICAL_SECTION = 10

# Shared variables
flag = [-1] * number_of_processes # Flags to indicate a process's current level
turn = [0] * (number_of_processes - 1)  # Turn array for each level
counter = 0  # Shared resource

def critical_section(process_id: int):
    """Critical section logic."""
    global counter
    c = counter
    print(f"Process {process_id}, Counter: {counter}")
    c += 1
    counter = c
    print(f"Process {process_id} exiting critical section, Counter: {counter}")

def peterson_n_process(process_id:int):
    """Implementation of Peterson's n-process algorithm."""
    global flag, turn

    # Entry Section
    for level in range(number_of_processes - 1):  # Compete at each level
        flag[process_id] = level  # Declare intent to enter level k
        turn[level] = process_id  # Assume it's my turn at level k
        for process_index in range(number_of_processes):
            if process_index != process_id:
                while flag[process_index] >= level and turn[level] == process_id:
                    pass  # Busy-wait

    # Critical Section
    critical_section(process_id)

    # Exit Section
    flag[process_id] = -1  # Indicate that the process is no longer competing

def run_task(process_id:int):
    """Simulates a single process executing multiple critical sections."""
    for _ in range(TIMES_TO_RUN_CRITICAL_SECTION):  # Repeat critical section 3 times
        peterson_n_process(process_id)

if __name__ == "__main__":
    t1 = time.time()
    with ThreadPoolExecutor(max_workers=number_of_processes) as executor:
        for i in range(number_of_processes):
            executor.submit(run_task, i)
    t2 = time.time()
    
    print(f"Took {t2-t1} seconds")
    print(f"Which is {(t2-t1)/60} mins")
