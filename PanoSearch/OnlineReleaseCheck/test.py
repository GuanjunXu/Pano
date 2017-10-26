import requests

for i in range(5000):
    r = requests.get(r"http://search.lekan.letv.com/lekan/panolanding_json.so?terminalApplication=supersearch&token=103XXXYG0JDaEbb5OFcndLviep03rYE5sI4gUlQqIVTYuAt4LKolRm3WGdUYeUGvpyY1kWm5bdSiFUjm23z8sAAVm5v1Dwm1vtzJ60eyqm1MNdOWBWvZfYIm4&coor=bd09ll&card_id=203-502-506-210-211-503-504-505-702-515&imei=861579030018148&ad_param=User-Agent%3Dandroid%252F6.0.1%2B%2528LeEco%253BLEX720%2529%2B%252F%252Faps_mm_00_1.1.3.6%252F15%26sspAdParameter%3D%2526uid%253D166720664%2526mid%253D2%25252C3%25252C5%25252C6%2526bm%253D166720664%2526cuid%253Dd34b1aee6f47bfd56a17c9a7f6020a47%2526brand%253DLeEco%2526model%253DLEX720%2526make%253DLeMobile%2526aid%253Dcfa4f28823c5fe0%2526mac1%253D020000000000%2526mac2%253DC8%25253A25%25253AE1%25253ABA%25253AE0%25253AA4%2526imei%253D861579030018148%2526dtype%253D0%2526uiv%253DLEX720_whole-netcom%2526os%253D0%2526zone%253DCN%2526loc%253Dzh_CN%2526tz%253DGMT%25252B08%25253A00%2526osv%253D6.0.1%2526net%253D2%2526reso%253D1080x1920%2526cv%253D3.0.2%2526sv%253D15%2526pkgn%253Dcom.letv.android.quicksearchbox%2526appn%253DPanoSearch%2526appc%253DIAB12-1%2526pcode%253DPanoSearch%2526cid%253D5%2526slotid%253D14524%2526sspid%253D1632%2526res%253Djson%2526fc%253D0%2526fd%253D1%2526scr%253D0%2526off%253D0%2526playid%253Dd34b1aee6f47bfd56a17c9a7f6020a47_1506069060569&terminalBrand=LeEco&video_history=29446276-27599655-30664366-20010820-1607552-30789733-1579598-30771732-22878445-30670849&sales_area=CN&lang=zh_cn&version=3.0.2&num=30&terminalSeries=LEX720_whole-netcom&pcode=160110000&music_history=&weather_city_code=01010101&longitude=116.49821101999638&mac=C825E1BAE0A4&bsChannel=letv_supersearch&from=mobile_super18&ad_session=2391c789ea084406a16d4aa66bd7a350-1506069060567&module_order_enable=1&user_setting_country=CN&latitude=39.94054976750015&uid=166720664&wcode=cn&devId=861579030018148")
    content = r.json()
    dd = content["data"]["home_page_module_order"][4]["records"][0]
    dataItemName = dd["action"]
    pkgname = dd["action"] # and 
    count = 0
    if dataItemName != "找工作" and '&package=&' not in pkgname:
        print("第%s次请求，没有应用新数据"%(i+1))
        count += 1
    if (i+1)%1000 == 0:
        print('%s times has been done.'%(i+1))

print("%s cases failed totally"%count)