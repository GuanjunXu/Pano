# -*- coding: utf-8

import json
import urllib
import os
import time
import xlrd
import random

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

test_versions = ['302', '303']

result_path = os.getcwd() + '\\result\\' + time.strftime("%Y-%m-%d_%H-%M-%S",time.localtime(time.time()))
try:
    os.makedirs(result_path)
except:
    pass

test_url = "http://220.181.1.151:8000/lekan/panolanding_json.so?terminalApplication=supersearch&token=&coor=bd09ll&card_id=203-521-522-523-502-506-210-211-503-504-505-702-515-901-903&imei=868897023472871&ad_param=User-Agent%3Dandroid%252F6.0%2B%2528LeEco%253BLeX620%2529%2B%252F%252Faps_mm_00_1.1.3.6%252F15%26sspAdParameter%3D%2526mid%253D2%25252C3%25252C5%25252C6%2526cuid%253Dd986432bd9bdabd296c3644e2fb6485e%2526brand%253DLeEco%2526model%253DLeX620%2526make%253DLeMobile%2526aid%253Dc16bdb79b6afa3c1%2526mac1%253D020000000000%2526mac2%253D84%25253A73%25253A03%25253AE7%25253ADC%25253AA0%2526imei%253D869552020002135%2526dtype%253D0%2526uiv%253DLe_X620_whole-netcom%2526os%253D0%2526zone%253DCN%2526loc%253Dzh_CN%2526tz%253DGMT%25252B08%25253A00%2526osv%253D6.0%2526net%253D2%2526reso%253D1080x1920%2526cv%253D3.0.2%2526sv%253D15%2526pkgn%253Dcom.letv.android.quicksearchbox%2526appn%253DPanoSearch%2526appc%253DIAB12-1%2526pcode%253DPanoSearch%2526cid%253D5%2526slotid%253D14524%2526sspid%253D1632%2526res%253Djson%2526fc%253D0%2526fd%253D1%2526scr%253D0%2526off%253D0%2526playid%253Dd986432bd9bdabd296c3644e2fb6485e_1502705471773&terminalBrand=LeEco&video_history=&sales_area=CN&lang=zh_cn&version=3.0.3&num=30&terminalSeries=Le_X620_whole-netcom&pcode=160110000&music_history=&weather_city_code=01010101&longitude=116.49819801016548&mac=847303E7DCA0&bsChannel=letv_supersearch&from=mobile_super18&ad_session=834a8af69e6e4ff89a4deaf728bad3f4-1502705471771&module_order_enable=1&user_setting_country=CN&latitude=39.94046478007413&uid=&wcode=cn&devId=868897023472871"
# "http://220.181.1.151:8000/lekan/panolanding_json.so?terminalApplication=supersearch&token=&coor=bd09ll&card_id=203-521-502-506-210-211-503-504-505-702-515-901-903&imei=868897023472871&ad_param=User-Agent%3Dandroid%252F6.0%2B%2528LeEco%253BLeX620%2529%2B%252F%252Faps_mm_00_1.1.3.6%252F15%26sspAdParameter%3D%2526mid%253D2%25252C3%25252C5%25252C6%2526cuid%253Dd986432bd9bdabd296c3644e2fb6485e%2526brand%253DLeEco%2526model%253DLeX620%2526make%253DLeMobile%2526aid%253Dc16bdb79b6afa3c1%2526mac1%253D020000000000%2526mac2%253D84%25253A73%25253A03%25253AE7%25253ADC%25253AA0%2526imei%253D869552020002135%2526dtype%253D0%2526uiv%253DLe_X620_whole-netcom%2526os%253D0%2526zone%253DCN%2526loc%253Dzh_CN%2526tz%253DGMT%25252B08%25253A00%2526osv%253D6.0%2526net%253D2%2526reso%253D1080x1920%2526cv%253D3.0.2%2526sv%253D15%2526pkgn%253Dcom.letv.android.quicksearchbox%2526appn%253DPanoSearch%2526appc%253DIAB12-1%2526pcode%253DPanoSearch%2526cid%253D5%2526slotid%253D14524%2526sspid%253D1632%2526res%253Djson%2526fc%253D0%2526fd%253D1%2526scr%253D0%2526off%253D0%2526playid%253Dd986432bd9bdabd296c3644e2fb6485e_1502705471773&terminalBrand=LeEco&video_history=&sales_area=CN&lang=zh_cn&version=3.0.2&num=30&terminalSeries=Le_X620_whole-netcom&pcode=160110000&music_history=&weather_city_code=01010101&longitude=116.49819801016548&mac=847303E7DCA0&bsChannel=letv_supersearch&from=mobile_super18&ad_session=834a8af69e6e4ff89a4deaf728bad3f4-1502705471771&module_order_enable=1&user_setting_country=CN&latitude=39.94046478007413&uid=&wcode=cn&devId=868897023472871"
# 10.11.165.204:7070
# 220.181.1.151:8000
# search.lekan.letv.com


file_name = "tracking.xlsx"
bk = xlrd.open_workbook(file_name)
case_sheet = bk.sheet_names()[0]
sh = bk.sheet_by_name(case_sheet)
nrows, ncols = sh.nrows, sh.ncols
col_names = sh.row_values(0)
start_line, end_line = 1, nrows

response = urllib.urlopen(test_url).read()
j_l = json.loads(response)

if j_l['data'] == {}:
    print "Request Failed"

def getByDepth(json_data, depth):
    test_module = json_data[depth[0]]
    try:
        for hie in depth[1:]:
            test_module = test_module[hie]
    except:
        pass
    return test_module

def getByText(json_data, t_t, text):
    i_t = 0
    t_t = t_t.lower()
    for d in json_data:
        if t_t not in d.keys():
            i_t += 1
            continue
        elif d[t_t] == text:
            break
        i_t += 1
    j_d = json_data[i_t]
    return j_d

def formatKV(kv, tag):
    kv_dict = {}
    k_list = []
    depth_three = ''
    if tag == 2:
        kv_sp = kv.split(':') # params
        depth_three = kv_sp[0]
        kv = kv_sp[1][1:-1]
    kv_l = kv.split(';')
    for kkvv in kv_l:
        if "=" in kkvv:
            kkvv_equ = kkvv.split('=')
            kv_dict[kkvv_equ[0]] = kkvv_equ[1]
        else:
            k_list.append(kkvv)
    return kv_dict, k_list, depth_three

def kvChecking(json_data, excel_kv_dict, excel_k_list, depth_three = None):
    if depth_three != None:
        json_data = json_data[depth_three]
    json_data_K = json_data.keys()
    fail_list = []
    if excel_k_list != []:
        for e_k in excel_k_list:
            if e_k not in json_data_K:
                fail_list.append(e_k)
    if excel_kv_dict != {}:
        excel_kv_dict_K = excel_kv_dict.keys()
        for e_d_k in excel_kv_dict_K:
            if e_d_k not in json_data_K:
                fail_list.append(e_d_k)
            elif excel_kv_dict[e_d_k] != str(json_data[e_d_k]):
                fail_list.append({e_d_k:excel_kv_dict[e_d_k]})
    return fail_list

def formatSpecKeys(spec_k):
    spec_k_list_new = spec_k.split(':')
    return spec_k_list_new

os.chdir(result_path)

for line in range(start_line, end_line):
    col_values = sh.row_values(line)
    k_v = dict(zip(col_names, col_values))
    if str(int(k_v['Ver'])) not in test_versions:
        continue
    print line, k_v['Summary'],
    test_result = 'Pass'
    fail_list = []
    tar_data = ''
    try:
        depth_one = k_v['Depth_1'].split(':')
        title = k_v['Title']
        data_one = getByDepth(j_l, depth_one)
        tar_data = getByText(data_one, 'Title', title)
    except:
        fail_list.append(title)
        test_result = 'Fail, title: %s not found'%fail_list
    if test_result == 'Pass':
        if k_v['Depth_2'] != '' and k_v['Ergodic'] == '':
            content = ''
            try:
                depth_two = k_v['Depth_2'].split(':')
                content_type = k_v['Content'].split(':')[0]
                content = k_v['Content'].split(':')[1]
                data_two = getByDepth(tar_data, depth_two)
                tar_data = getByText(data_two, content_type, content)
            except:
                fail_list.append(content)
                test_result = 'Fail, content/name: %s not found'%fail_list
        elif k_v['Ergodic'] != '':
            #continue
            try:
                depth_two = k_v['Depth_2'].split(':')
                data_two = getByDepth(tar_data, depth_two)
                tar_data = random.choice(data_two)
            except:
                fail_list.append(depth_two)
                test_result = 'Fail, content/name: %s not found'%fail_list
        if test_result == 'Pass':
            if k_v['VerifyKV_1'] != '':
                fkv_ret = formatKV(k_v['VerifyKV_1'], 1)
                kv_dict, k_list = fkv_ret[0], fkv_ret[1]
                check_result = kvChecking(tar_data, kv_dict, k_list)
                if check_result != []:
                    fail_list.append(check_result)
                    test_result = 'Fail, %s not found'%fail_list
            if k_v['VerifyKV_2'] != '':
                fkv_ret = formatKV(k_v['VerifyKV_2'], 2)
                kv_dict, k_list, depth_three = fkv_ret[0], fkv_ret[1], fkv_ret[2]
                check_result = kvChecking(tar_data, kv_dict, k_list, depth_three)
                if check_result != []:
                    fail_list.append(check_result)
                    test_result = 'Fail, %s not found'%fail_list
            if k_v['Spec_K'] != '':
                spec_k = k_v['Spec_K']
                spec_k_new = [spec_k]
                if ';' in spec_k:
            	    spec_k_new = spec_k.split(';')
                for speck in spec_k_new:
                    spk_list = formatSpecKeys(speck)
                    depth_four, kk, key_toverify = spk_list[0], spk_list[1] + '=', spk_list[2]
                    spec_full = tar_data[depth_four]
                    json_spec_ks = spec_full.split(kk)[1]
                    json_spec_k_list = json_spec_ks.split(',')
                    excel_spec_k_list = key_toverify.split(',')
                    for k in excel_spec_k_list:
                        if k not in json_spec_k_list and k not in spec_k: #json_spec_ks:
                            fail_list.append(k)
                            test_result = 'Fail, %s not found'%fail_list
    print "\t" + test_result.decode("unicode-escape") + "\n" + "-"*10
    f = open('%s_%s_%s.txt'%(line, test_result[:4], k_v['Summary']), 'w')
    f.write('*****Excel data*****:\n' + str(k_v).decode("unicode-escape") + '\n\n\n' + test_result.decode("unicode-escape") + '\n\n\n' + '*****Json data*****:\n' + str(tar_data).decode("unicode-escape"))
    f.close()