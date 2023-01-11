import os
def fileasdir(path):
    d=path
    res={}
    for root,dire,files  in os.walk(d):
        for d in dire:
            res[d]=os.listdir(root + "/"+d)
    print(res)
address=input("enter the file path:")
fileasdir(address)


