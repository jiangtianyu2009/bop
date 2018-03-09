from PIL import Image
import numpy as np
import os
import shutil
from ImgResize import imgresize

baseurl = r'C:\Users\jiangt6\Downloads\test'
disturl = r'C:\Users\jiangt6\Downloads\test-dst'
files = os.listdir(baseurl)

ranger = 5
nameer = 100
countr = 0

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

dstcounter = 6000
dstdir = os.listdir(disturl)
for dirr in dstdir:
    files = os.listdir(disturl + os.sep + dirr)
    baseimg = imgresize(Image.open(
        disturl + os.sep + dirr + os.sep + files[0]))
    basemat = np.atleast_2d(baseimg)
    for file in files[1:]:
        print('Appending ' + file)
        appendimg = imgresize(Image.open(
            disturl + os.sep + dirr + os.sep + file))
        appendmat = np.atleast_2d(appendimg)
        basemat = np.append(basemat, appendmat, axis=0)
    report_img = Image.fromarray(basemat)
    report_img.save(disturl + os.sep + str(dstcounter) + '.jpg')
    print('Save Pic ' + str(dstcounter) + '.jpg')
    dstcounter = dstcounter + 1
