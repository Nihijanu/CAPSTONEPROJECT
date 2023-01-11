from time import sleep,perf_counter
from threading import Thread
def task1():
    for i in range(4):
        print("i am task 1 start ")
        sleep(1)
    #print("task 1 end")
def task2():
    for i in range(4):
        print("i am task 2 start ")
        sleep(1)
    print("task 2 end")
start_time=perf_counter()
t1=Thread(target=task1)
t2=Thread(target=task2)
t1.start()
t2.start()
t1.join()
t2.join()
end_time=perf_counter()
print(f'{end_time-start_time} seconds taken')
