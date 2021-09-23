
# Threading = a flow of execution. Like a separate order of instructions
#               However each thread takes a turn running to achieve concurrency
#               GIL = (global interpreter lock)
#               allows only one thread to hold the control of the Python interpreter at any one time

# CPU bound = program/task spends most of its time waiting for internal events (CPU intensive)
#               use multiprocessing

# io bound = program/task spends most of its time waiting for external events (user input, web scraping)
#               use multithreading


import time
import threading


def study():
    time.sleep(3)
    print("studying")


def eat():
    time.sleep(4)
    print("eating")


def drink():
    time.sleep(5)
    print("drinking coffee")



x = threading.Thread(target=drink(), args=())
x.start()

y = threading.Thread(target=eat, args=())
y.start()

z = threading.Thread(target=study, args=())
z.start()

x.join()
y.join()
z.join()
print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())