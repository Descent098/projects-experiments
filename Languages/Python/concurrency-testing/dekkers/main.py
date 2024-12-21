from concurrent.futures import ThreadPoolExecutor
import random
import time
turn = 0
wants_to_enter = [False, False]

def dekkers(process_id:int, other_id:int):
    global wants_to_enter, turn
    print(f"Entering Dekkers() with thread {process_id}")
    time.sleep(random.randint(0,2)) # adding randomness to pontentially mess up ordering
    wants_to_enter[process_id] = True
 
    while wants_to_enter[other_id]:
        if turn != process_id:
            wants_to_enter[process_id] = False
            while turn != process_id:
                ... # busy wait
        wants_to_enter[process_id] = True

	# critical section
    ...

    turn = other_id
    wants_to_enter[process_id] = False
	# remainder section
    print(f"Exiting Dekkers() with thread {process_id}")

if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(dekkers, 0,1)
        executor.submit(dekkers, 1,0)