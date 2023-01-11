import os

# dir=os.getcwd()
# file=os.listdir(dir)
# files=[f for f in file if os.path.isfile(dir + '/'+f)]
# print(files)
# fpy=[f for f in  file if f.endswith(".py")]
# print(fpy)


import os
#drive=os.system('cmd /c "wmic logicaldisk list brief')
def driveee():
    drive = os.popen("fsutil fsinfo drives").read()
    print(drive)


