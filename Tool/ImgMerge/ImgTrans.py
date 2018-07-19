import os
import shutil
import tkinter.filedialog

import numpy as np
from PIL import Image, ImageFile

from ImgResize import imgresize

ImageFile.LOAD_TRUNCATED_IMAGES = True
root = tkinter.Tk()
root.withdraw()
dirname = tkinter.filedialog.askdirectory(
    parent=root, initialdir=r'C:\jty\HM', title='Please select a directory')
if len(dirname) > 0:
    print("You choosed %s" % dirname)
    baseurl = dirname
    disturl = dirname + '-dst'
    if not os.path.exists(disturl):
        os.mkdir(disturl)


files = os.listdir(baseurl)

dstcounter = 6000


for file in files:

    print('Image ' + file)
    baseimg = imgresize(Image.open(
        baseurl + os.sep + file).convert('RGB'))
    basemat = np.atleast_2d(baseimg)

    report_img = Image.fromarray(basemat)
    report_img.save(disturl + os.sep + str(dstcounter) + '.jpg')
    print('Save Pic ' + str(dstcounter) + '.jpg')
    print()
    dstcounter = dstcounter + 1
