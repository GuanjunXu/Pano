# -*- coding: utf-8

import json
import urllib
import os
import time
import random

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

test_url = "http://220.181.1.151:8080/lekan/panolanding_json.so?terminalApplication=supersearch&token=&coor=bd09ll&card_id=203-521-522-523-502-506-210-211-503-504-505-702-515-901-903&imei=868897023472871&ad_param=User-Agent%3Dandroid%252F6.0%2B%2528LeEco%253BLeX620%2529%2B%252F%252Faps_mm_00_1.1.3.6%252F15%26sspAdParameter%3D%2526mid%253D2%25252C3%25252C5%25252C6%2526cuid%253Dd986432bd9bdabd296c3644e2fb6485e%2526brand%253DLeEco%2526model%253DLeX620%2526make%253DLeMobile%2526aid%253Dc16bdb79b6afa3c1%2526mac1%253D020000000000%2526mac2%253D84%25253A73%25253A03%25253AE7%25253ADC%25253AA0%2526imei%253D869552020002135%2526dtype%253D0%2526uiv%253DLe_X620_whole-netcom%2526os%253D0%2526zone%253DCN%2526loc%253Dzh_CN%2526tz%253DGMT%25252B08%25253A00%2526osv%253D6.0%2526net%253D2%2526reso%253D1080x1920%2526cv%253D3.0.2%2526sv%253D15%2526pkgn%253Dcom.letv.android.quicksearchbox%2526appn%253DPanoSearch%2526appc%253DIAB12-1%2526pcode%253DPanoSearch%2526cid%253D5%2526slotid%253D14524%2526sspid%253D1632%2526res%253Djson%2526fc%253D0%2526fd%253D1%2526scr%253D0%2526off%253D0%2526playid%253Dd986432bd9bdabd296c3644e2fb6485e_1502705471773&terminalBrand=LeEco&video_history=&sales_area=CN&lang=zh_cn&version=3.0.3&num=30&terminalSeries=Le_X620_whole-netcom&pcode=160110000&music_history=&weather_city_code=01010101&longitude=116.49819801016548&mac=847303E7DCA0&bsChannel=letv_supersearch&from=mobile_super18&ad_session=834a8af69e6e4ff89a4deaf728bad3f4-1502705471771&module_order_enable=1&user_setting_country=CN&latitude=39.94046478007413&uid=&wcode=cn&devId=868897023472871"

tacking_path = os.getcwd() + '\\ali_game_tracking_results\\' + time.strftime("%Y-%m-%d_%H-%M-%S",time.localtime(time.time()))

try:
    os.makedirs(tacking_path)
except:
    pass

os.chdir(tacking_path)

for i in range(500):
    print "# %s times tracking... %s "%(i,time.strftime("%Y-%m-%d_%H-%M-%S",time.localtime(time.time())))
    response = urllib.urlopen(test_url).read()
    j_l = json.loads(response)
    #
    if j_l['data'] == {}:
        print "Request Failed"
    #
    all_cards = j_l['data']['home_page_module_order']
    for card in all_cards:
        try:
            if card['title'] == '您的好友正在玩':
                game_card = card
                break
        except:
            pass
    #
    game_data = game_card['records']
    f = open(time.strftime("%Y-%m-%d_%H-%M-%S",time.localtime(time.time())) + '.txt', 'w')
    #game_data_format = ''
    for g in game_data:
        f.write(str(g['content']) + '\n' + g['params']['gid'] + '\n\n') #.decode("unicode-escape") + '\n')
    #f.write(game_data_format) #str(game_data_format).decode("unicode-escape"))
    f.close()
    print "\thold 15mins..."
    time.sleep(60*15)