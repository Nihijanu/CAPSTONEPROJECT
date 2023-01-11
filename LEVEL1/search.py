import os
from time import perf_counter
start=perf_counter()
def find (filename,path):
    res=[]
    for root , dirs,files in os.walk(path):
        for name in files:
            if name==filename:
                print("file exist")
                break

name="os.py"
dir ="C:\CAPSTONEPROJECT"
find(name,dir)
end=perf_counter()
print(f'{end-start} time taken')
