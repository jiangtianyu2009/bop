import os
import re
import shutil

baseurl = r'C:\Users\jiangt6\Downloads\合集'
resturl = r'C:\Users\jiangt6\Downloads\snyh'

folders = os.listdir(baseurl)
for folder in folders:
    subfolders = os.listdir(baseurl + os.sep + folder)
    for subfolder in subfolders:
        print('Move ' + str(subfolder))
        shutil.move(baseurl + os.sep + folder + os.sep + subfolder, resturl)
