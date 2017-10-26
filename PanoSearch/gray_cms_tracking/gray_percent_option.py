# -*- coding: utf-8

import json
import urllib
import os
import time
import random

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

gray_url = "http://t-gray-mob-app.le.com/gray/list?pcode=160110016&version=3.5&model=Le&sys=3.5&areainfo=16&isIp=0&devid="

imei_list_str = open('imei_list.txt', 'r').read()
imei_list = imei_list_str[1:-1].split(',')

on_count = 0

imei = 861795230055999

# for imei in imei_list:
for i in range(10000):
    full_url = gray_url + str(imei) #[1:-1]
    response = urllib.urlopen(full_url).read()
    j_l = json.loads(response)
    Pano_status = j_l['data']['Pano_203']
    if Pano_status == '1':
        on_count += 1
        print '\n' + str(imei) + '\t' + Pano_status #[1:-1]
    else:
        print '.',
    imei += 1

print '\n*******************\nCovered: %s'%on_count