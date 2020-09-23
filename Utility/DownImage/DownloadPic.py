import os
import re
import shutil
import urllib.request

import bs4
import requests

base_url = 'https://www.goldenshark.me/images/'
srcDirList = [r'C:\jty\xunlei\process']
p = re.compile(r'(\D+)(\d+)')


def addSep(filename):
    fhalf = p.search(filename).group(1).upper()
    mhalf = p.search(filename).group(2).upper()
    lhalf = '.jpg'
    distname = fhalf + '-' + mhalf + lhalf
    return distname


for srcDir in srcDirList:
    filenames = os.listdir(srcDir)
    for filename in filenames:
        preFileName = filename.split(".")[0]
        if preFileName[-1] == "A" or preFileName[-1] == "B" or preFileName[-1] == "C":
            preFileName = preFileName[0:len(preFileName) - 1]
        destPicName = srcDir + os.sep + preFileName + '.jpg'
        if os.path.isfile(destPicName):
            print(destPicName + ' already here.\n')
        else:
            full_url = base_url + addSep(preFileName)
            try:
                print(preFileName + "\n" + full_url)
                print(destPicName + "\n")
                if not os.path.isfile(destPicName):
                    urllib.request.urlretrieve(full_url, destPicName)
            except:
                print('!!!!!!!!!!!!!! Can not find picture of ' +
                      filename + ' !!!!!!!!!!!!!!\n')
