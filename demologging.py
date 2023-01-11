import logging
logging.basicConfig(filename='logfile.txt',level=logging.WARNING)
class FileLog:
    def __int__(self):
           pass

    def Operation(self):
        try:
                self. x=int(input("Enter the firstnumber"))
                self.y=int(input("Enter Second Number"))
                print(self.x/self.y)
        except ZeroDivisionError as msg:
            logging.exception(msg)
        except ValueError as msg:
            logging.exception(msg)
if __name__=='__main__':
    f=FileLog()
    f.Operation()
