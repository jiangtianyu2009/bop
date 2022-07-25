import os
import random
import re
import shutil
import threading
import time
import urllib.request

import bs4
import requests
from click import command

base_url = 'https://i3.nhentai.net/galleries/'
srcDirList = [r'H:\temp\TC']
srcDir = r'H:\temp'


def downloadImage(comic_id, num):
    comic_id = str(comic_id)
    for i in range(1, num + 1):
        imgNamePrefix = str(i)
        fileNamePrefix = str(i).zfill(3)

        if not os.path.isdir(srcDir + os.sep + comic_id):
            os.makedirs(srcDir + os.sep + comic_id)

        destImagePath = srcDir + os.sep + comic_id + os.sep + fileNamePrefix + '.jpg'
        imgSrc = base_url + comic_id + '/' + imgNamePrefix + '.jpg'
        # Check Whether Image Exists
        if os.path.isfile(destImagePath):
            print(destImagePath + ' already here.\n')
        else:
            # Download Image
            try:
                print('Desti file path: ' + destImagePath)
                if not os.path.isfile(destImagePath):
                    opener = urllib.request.build_opener()
                    opener.addheaders = [(
                        'User-Agent',
                        'Mozilla/5.0 (Windows NT 6.1; WOW64) \
                        AppleWebKit/537.36 (KHTML, like Gecko) \
                        Chrome/66.0.1941.0 Safari/537.36')]
                    urllib.request.install_opener(opener)
                    urllib.request.urlretrieve(imgSrc, destImagePath)
            except:
                print(destImagePath + 'download failed!')
            print('=======================================')


if __name__ == '__main__':
    downloadImage(1859331, 135)
