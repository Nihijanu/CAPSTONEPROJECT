import logging


class Demologging():

    def __int__(self):
        logging.basicConfig(filemode='logfile.txt',level=logging.WARNING)

    def Operations(self):
        try:
            self.x=int(input("enter"))
            self.y = int(input("enter"))
            print(self.x/self.y)
        except ZeroDivisionError as msg:
            logging.exception(msg)
        except ValueError as msg:
            logging.exception(msg)


obj=Demologging()
obj.Operations()
