# import multiprocessing as mp
# print("no of process:",mp.cpu_count())

from time import perf_counter
from threading import Thread
from LEVEL1.os import driveee
from LEVEL1.search1 import drive_search
s = perf_counter()
drivee = input("enter drive")
inp = input("searching for")
t1 = Thread(target=driveee)
t2 = Thread(target=drive_search(drivee, inp))
t1.start()
t2.start()
t1.join()
t2.join()
e = perf_counter()
print(f'{e-s} time taken')
