import os
import re
import shutil

baseurl = r'C:\Users\jiangt6\Downloads\韩漫1\Desire King\01-53'
resturl = r'C:\Users\jiangt6\Downloads\韩漫1\Desire King\01-53-combine'
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
