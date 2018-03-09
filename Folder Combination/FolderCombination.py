import os
import re
import shutil

baseurl = r'C:\Users\jiangt6\Downloads\韩漫\恋爱辅助器\01-111'
resturl = r'C:\Users\jiangt6\Downloads\韩漫\恋爱辅助器\01-111-combine'
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
