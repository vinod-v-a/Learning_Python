"""
============================= multithreading =======================================
The threading module provides a way to run multiple threads (smaller units of a process) concurrently within a single process.
It allows for the creation and management of threads, making it possible to execute tasks in parallel, sharing memory space.
Threads are particularly useful when tasks are I/O bound, such as file operations or making network requests,
where much of the time is spent waiting for external resources.
"""

# import threading
#
# import time
#
#
# def func(x):
#     print(f"before sleeping - {x}")
#     time.sleep(1)
#     print(f"after sleeping - {x}")
#
#
# "Normal Execution"
# # start = time.time()
# # func("first")
# # func("second")
# # stop = time.time()
# # print(f"total time took for execution - {round(stop - start, 2)}")
#
#
# "Using multithreading "
# t1 = threading.Thread(target=func, args=("first",))
# t2 = threading.Thread(target=func, args=("second",))
#
# start = time.time()
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()
#
# stop = time.time()
# print(f"\ntotal time took for execution - {round(stop-start, 2)}")

"==================== Checking Multithreading in single Process ==============="

import time
import threading
import os

start = time.time()

def sleeping_function():
    print('Sleeping 1 second...')
    time.sleep(1)
    print('Done Sleeping...')
    print('Process ID:', os.getpid())
    print('Thread ID:', threading.get_ident(), '\n')


"Normal method"
# sleeping_function()
# sleeping_function()
#
# finish = time.time()
#
# print(f'Finished in {round(finish - start, 2)} seconds')

"========= Using Multithreading ================"
# t1 = threading.Thread(target=sleeping_function)
# t2 = threading.Thread(target=sleeping_function)
#
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()
# finish = time.time()
#
# print(f'Finished in {(finish - start)} seconds')


"======== Using Loop =========="
# Another way

# threads = []
# for _ in range(10):
#     t = threading.Thread(target=sleeping_function)
#     t.start()
#     threads.append(t)
# for each in threads:
#     each.join()
# finish = time.time()
#
# print(f'Finished in {round(finish - start, 2)} seconds')


"""
===================== multiprocessing ======================
Multiprocessing refers to the ability of a system to support more than one processor at the same time. 
Applications in a multiprocessing system are broken to smaller routines that run independently. 
The operating system allocates these threads to the processors improving performance of the system.
"""


import time
import multiprocessing
import os


start = time.time()


def sleeping_function():
    print('Sleeping 1 second...')
    time.sleep(1)
    print('Done Sleeping...')
    print('process id:', os.getpid(), '\n')


# if __name__ == "__main__":
#     pr1 = multiprocessing.Process(target=sleeping_function)
#     pr2 = multiprocessing.Process(target=sleeping_function)
#
#     pr1.start()
#     pr2.start()
#
#     pr1.join()
#     pr2.join()
#
#     finish = time.time()
#
#     print(f'Finished in {round(finish - start, 2)} seconds')


"Another Way"
if __name__ == "__main__":

    process = []

    for _ in range(10):
        pr = multiprocessing.Process(target=sleeping_function)
        pr.start()
        process.append(pr)
    for each_process in process:
        each_process.join()
    finish = time.time()

    print(f'Finished in {round(finish - start, 2)} seconds')




