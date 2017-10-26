import sys
import os
import random

gen_list = []
gen_first = 800000000000000
gen_tag = ''

f = open('imei_list.txt', 'w')

if len(sys.argv) < 2:
    print("Script must run with params(e.g.: python generate_imei_list.py 1000 80000000 &).")
    sys.exit()
else:
    gen_count = int(sys.argv[1]) # 第一个参数为生成个数
    try:
        gen_first = int(sys.argv[2]) # 第二个参数为起始数
        gen_tag = sys.argv[3] # 第三个参数为每个IMEI两端是否添加标记（如引号）
    except:
        pass
    gen_imei = gen_first
    for i in range(gen_count):
        # print(str(gen_imei),',',end = '')
        imei_to = gen_tag + str(gen_imei) + gen_tag # 逐个生成的imei两侧添加冒号类标记
        gen_list.append(imei_to)
        gen_imei += 1
    f.write(str(gen_list))
    f.close()