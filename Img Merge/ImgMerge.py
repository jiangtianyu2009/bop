from PIL import Image
import numpy as np
import os
import shutil

baseurl = r'C:\Users\jiangt6\Downloads\韩漫2\危险性游戏\1-25-combine'
disturl = r'C:\Users\jiangt6\Downloads\韩漫2\危险性游戏\1-25-dst'
files = os.listdir(baseurl)

countr = 0
ranger = 16
nameer = 100

for file in files:
    if file in files[ranger * countr: ranger * countr + ranger]:
        pass
    else:
        countr = countr + 1
        nameer = nameer + 1
    if not os.path.exists(disturl + os.sep + str(nameer)):
        os.mkdir(disturl + os.sep + str(nameer))
    shutil.copy(baseurl + os.sep + file, disturl +
                os.sep + str(nameer) + os.sep + file)

dstcounter = 800
dstdir = os.listdir(disturl)
for dirr in dstdir:
    files = os.listdir(disturl + os.sep + dirr)
    baseimg = Image.open(disturl + os.sep + dirr + os.sep + files[0])
    sz = baseimg.size
    basemat = np.atleast_2d(baseimg)
    for file in files[1:]:
        print('Appending ' + file)
        im = Image.open(disturl + os.sep + dirr + os.sep + file)
        mat = np.atleast_2d(im)
        basemat = np.append(basemat, mat, axis=0)
    report_img = Image.fromarray(basemat)
    report_img.save(disturl + os.sep + str(dstcounter) + '.jpg')
    print('Save Pic ' + str(dstcounter) + '.jpg')
    dstcounter = dstcounter + 1
