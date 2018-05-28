import os
import re
import shutil
import tkinter.filedialog

root = tkinter.Tk()
root.withdraw()
dirname = tkinter.filedialog.askdirectory(
    parent=root, initialdir=r'C:\jty\HM', title='Please select a directory')
if len(dirname) > 0:
    print("You choosed %s" % dirname)
    baseurl = dirname
    resturl = dirname + '-combine'
    if not os.path.exists(resturl):
        os.mkdir(resturl)

distDirList = os.listdir(baseurl)
countnum = 1001

for distDir in distDirList:
    filenames = os.listdir(baseurl + os.sep + distDir)
    print(distDir)
    print(filenames)
    for filename in filenames:
        postfix = os.path.splitext(filename)[1]
        shutil.copy(baseurl + os.sep + distDir + os.sep + filename,
                    resturl + os.sep + str(countnum) + postfix)
        countnum = countnum + 1
