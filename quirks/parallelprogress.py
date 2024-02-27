########################
# A Program to create progress bar for parallel program
########################

import multiprocessing as mp
import tqdm
from time import sleep

cpu_count = mp.cpu_count() - 1
tasks = range(35)

def do_work(task):
    sleep(1)
    return task

# THIS IS IMPORTANT
# In windows, all the subprocesses import the calling scripts for the dependencies
# adding name = main stops subprocesses to recursively generate further subprocesses
# so, the time.sleep function is present
if __name__ == "__main__":
    try:
        with mp.Pool(processes=cpu_count) as pool:
            mapped_values = list(tqdm.tqdm(pool.imap_unordered(do_work, tasks), total=len(tasks)))
            pool.close()

        print(mapped_values)
    except Exception as e:
        print(e)