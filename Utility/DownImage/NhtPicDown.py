import os
import random
import re
import shutil
import threading
import time
import urllib.request
import multiprocessing
import bs4
import requests
from click import command

base_url = 'https://i7.nhentai.net/galleries/'
srcDirList = [r'H:\temp\TC']
srcDir = r'H:\temp'


def download_image(args_item):
    (comic_id, pic_index) = args_item
    imgNamePrefix = str(pic_index)
    fileNamePrefix = str(pic_index).zfill(3)
    # Build desti file name and path
    destImagePath = srcDir + os.sep + \
        str(comic_id) + os.sep + fileNamePrefix + '.jpg'
    imgSrc = base_url + str(comic_id) + '/' + imgNamePrefix + '.jpg'
    # Check Whether Image Exists
    if os.path.isfile(destImagePath):
        print(destImagePath + ' already here.')
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
            print(destImagePath + ' download complete!')
        except:
            print(destImagePath + ' download failed!')


def thread_download(args_list):
    try:
        pool = multiprocessing.Pool()
        res = pool.map(download_image, args_list)
        pool.close()
        pool.join()
    except:
        print("Error: unable to start thread")


if __name__ == '__main__':
    comic_id = 1859331
    pic_count = 135

    # Create dir if not exist
    if not os.path.isdir(srcDir + os.sep + str(comic_id)):
        os.makedirs(srcDir + os.sep + str(comic_id))

    args_list = []
    for i in range(1, pic_count + 1):
        args_list.append((comic_id, i))
    thread_download(args_list)
