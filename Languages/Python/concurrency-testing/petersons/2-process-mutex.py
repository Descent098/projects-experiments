# This is an alternative version of the same code, but using a mutex instead
from threading import Lock
from concurrent.futures import ThreadPoolExecutor

turn = Lock()
counter = 0

def critical_section(process_id:int):
    global counter
    print(f"In the critical section for {process_id}, and counter is {counter}")
    counter += 100
    print(f"Exiting the critical section for {process_id}, and counter is {counter}")


def run_thread(process_id:int):
    global counter
    print(f"Starting {process_id}, and counter is {counter}")
    completed = 0
    while completed < 100:
        with turn:
            critical_section(process_id)
        completed+=1
    
if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(run_thread, 0)
        executor.submit(run_thread, 1)
