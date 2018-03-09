import os
import re
import shutil

baseurl = r'C:\Users\jiangt6\Downloads\韩漫\17种性幻想\1-63'
resturl = r'C:\Users\jiangt6\Downloads\韩漫\17种性幻想\1-63-combine'
distDirList = os.listdir(baseurl)
countnum = 1001

for distDir in distDirList:
    filenames = os.listdir(baseurl + os.sep + distDir)
    print(distDir)
    print(filenames)
    for filename in filenames:
        shutil.copy(baseurl + os.sep + distDir + os.sep + filename,
                    resturl + os.sep + str(countnum) + '.jpg')
        countnum = countnum + 1
