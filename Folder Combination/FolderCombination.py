import os
import re
import shutil

baseurl = r'C:\Users\jiangt6\Downloads\韩漫\诱惑第一季\1-38\\'
resturl = r'C:\Users\jiangt6\Downloads\韩漫\诱惑第一季\1-38-combine\\'
distDirList = os.listdir(baseurl)
countnum = 1001

for distDir in distDirList:
    filenames = os.listdir(baseurl + distDir)
    print(distDir)
    print(filenames)
    for filename in filenames:
        shutil.copy(baseurl + distDir + os.sep + filename,
                    resturl + str(countnum) + '.jpg')
        countnum = countnum + 1
