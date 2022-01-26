# Sets start time
from time import time, sleep

start_time = time()
sleep(20)
end_time = time()

tot_time = end_time - start_time
print("\nTotal Elapsed Runtime:", tot_time, "in seconds.")
