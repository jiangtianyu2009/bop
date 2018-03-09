from PIL import Image
from ImgResize import imgresize
import numpy as np
import os
import shutil


baseurl = r'C:\Users\jiangt6\Downloads\韩漫\恋爱辅助器\01-111-combine'
disturl = r'C:\Users\jiangt6\Downloads\韩漫\恋爱辅助器\01-111-dst'
files = os.listdir(baseurl)


dstcounter = 6000

maxjpgdim = 50000
curjpgdim = 0

sectionstartfile = True

for file in files:

    if sectionstartfile:
        print('Base Image ' + file)
        baseimg = imgresize(Image.open(baseurl + os.sep + file))
        curjpgdim = baseimg.size[1]
        basemat = np.atleast_2d(baseimg)
        sectionstartfile = False
    else:
        print('Appending Image ' + file)
        appendimg = imgresize(Image.open(baseurl + os.sep + file))
        curjpgdim = curjpgdim + appendimg.size[1]
        appendmat = np.atleast_2d(appendimg)
        basemat = np.append(basemat, appendmat, axis=0)
        if curjpgdim > maxjpgdim:
            print('Current JPG Dim: ' + str(curjpgdim))
            report_img = Image.fromarray(basemat)
            report_img.save(disturl + os.sep + str(dstcounter) + '.jpg')
            print('Save Pic ' + str(dstcounter) + '.jpg')
            print('********************************************')
            print()
            dstcounter = dstcounter + 1
            sectionstartfile = True

report_img = Image.fromarray(basemat)
report_img.save(disturl + os.sep + str(dstcounter) + '.jpg')
print('Save Pic ' + str(dstcounter) + '.jpg')
dstcounter = dstcounter + 1
