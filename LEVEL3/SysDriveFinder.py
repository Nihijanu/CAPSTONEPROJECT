import  os
class Systemfinder:
    def __int__(self):
        pass

    def find_dirves(self):
        print("This is the drives method")
        drives=[]
        for x in range(65,91):
            if os.path.exists(chr(x)+":"):
                drives.append(chr(x))
        return drives
if __name__=="__main__":
    obj=Systemfinder()
    print(obj.find_dirves())