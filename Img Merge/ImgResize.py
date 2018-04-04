import numpy as np
from PIL import Image


defaultwidth = 720


def imgresize(imagefile):
    imagesize = imagefile.size
    print('Width: ' + str(imagesize[0]) +
          ' // ' + 'Heitht: ' + str(imagesize[1]))
    if imagesize[0] != defaultwidth:
        imagefile = imagefile.resize((defaultwidth, round(
            imagesize[1] / imagesize[0] * defaultwidth)), Image.ANTIALIAS)
        imagesize = imagefile.size
        print('Resize to: ' + 'Width: ' +
              str(imagesize[0]) + ' // ' + 'Heitht: ' + str(imagesize[1]))
    print()
    return imagefile
