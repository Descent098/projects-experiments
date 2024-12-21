from concurrent.futures import ThreadPoolExecutor

turn = 0
counter = 0
flag = [False, False]

def critical_section(process_id:int):
    global counter
    print(f"In the critical section for {process_id}, and counter is {counter}")
    counter += 100
    print(f"Exiting the critical section for {process_id}, and counter is {counter}")


def petersons(current_thread_id:int = 0, other_thread_id:int=1):
    global turn, flag, counter
    print(f"Entering petersons() in thread {current_thread_id}, and counter is {counter}")
    
    completed = 0
    TIMES_TO_RUN_CRITICAL_SECTION = 100
    
    while completed < TIMES_TO_RUN_CRITICAL_SECTION:
        print(f"In petersons(), in thread {current_thread_id}, loop #{completed+1} and counter is {counter}")
        flag[current_thread_id] = True
        turn = other_thread_id
        while (flag[other_thread_id] and turn == other_thread_id):
            ... # Busy wait

        # Critical Section
        critical_section(current_thread_id)
        
        flag[current_thread_id] = False
        # Remainder section
        completed += 1

    print(f"Exiting petersons() in thread {current_thread_id}, and counter is {counter}")

def run_thread(process_id:int):
    global counter
    print(f"Starting {process_id}, and counter is {counter}")
    if process_id == 0:
        petersons(0, 1)
    else:
        petersons(1, 0)
    
if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(run_thread, 0)
        executor.submit(run_thread, 1)
