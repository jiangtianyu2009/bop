from PIL import Image
from ImgResize import imgresize
import numpy as np
import os
import shutil
import tkinter.filedialog

root = tkinter.Tk()
root.withdraw()
dirname = tkinter.filedialog.askdirectory(
    parent=root, initialdir=r'C:\jty\Pic', title='Please select a directory')
if len(dirname) > 0:
    print("You choosed %s" % dirname)
    baseurl = dirname
    disturl = dirname + '-dst'
    if not os.path.exists(disturl):
        os.mkdir(disturl)


files = os.listdir(baseurl)

dstcounter = 6000
maxjpgdim = 50000
curjpgdim = 0

sectionstartfile = True

for file in files:

    if sectionstartfile:
        print('Base Image ' + file)
        baseimg = imgresize(Image.open(
            baseurl + os.sep + file).convert('RGB'))
        curjpgdim = baseimg.size[1]
        basemat = np.atleast_2d(baseimg)
        sectionstartfile = False
    else:
        print('Appending Image ' + file)
        appendimg = imgresize(Image.open(
            baseurl + os.sep + file).convert('RGB'))
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
