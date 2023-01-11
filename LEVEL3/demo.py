import os
import threading
class Filesearcher(threading.Thread):
    drive=""
    file_name=""
    def __int__(self):
        pass
    def seatch_for_file(self,drive,file_name):
        try:
            print("this is a file searcher")
            file_paths=[]
            drv=drive+":\\"
            print(drv)
            for root,dirs,files in os.walk(drv):
                for name in files:
                    if name==file_name:
                        path=os.path.abspath(os.path.join(root,name))
                        file_paths.append(path)
        except:
            print("there was an error")
        return file_paths
    def run(self):
        self.seatch_for_file(self.drive,self.file_name)
if __name__=='__main__':
    obj=Filesearcher()
    print(obj.seatch_for_file("C","ufhgg"))