import os
from time import perf_counter
def drive_search(drive,inp):
    counter=0
    for r,d,f in os.walk(drive):
        for file in f:
            filepath=os.path.join(r,file)
            if inp in file:
                counter +=1
                print(filepath)
    if counter==0:
        print("No file found")
    else:
        print(f"{counter} files found")

# start_=perf_counter()
#
# drivee=input("enter drive")
# inp = input("searching for")
# drive_search(drivee)
# end_=perf_counter()
# print(f'time taken to perform:{end_ -start_} seconds')