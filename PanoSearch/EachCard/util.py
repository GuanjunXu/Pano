import requests


def getAllCards(js_data, depth):
    # 传入depth，以冒号隔开，如："data:home_page_module_order"
    deep = depth.split(':')
    test_data = js_data[deep[0]]
    try:
        for d in deep[1:]:
            test_data = test_data[d]
    except:
        pass
    return test_data


def getDataByText(test_data, target_text):
    for data in test_data:
        try:
            if data['title'] == target_text:
                return data
        except:
            pass


def checkField(test_field, test_data, target_data, fail_list=[], data_id=None):
    '''
        若目标值不为''，判断是否与测试数据的值相等，不等加入fail队列
        若目标值为''或' '，判断测试数据的值是否为空，为空加入fail队列
    '''
    if target_data != '':
        if type(test_field[test_data]) != type(target_data):
            if data_id != None:
                fail_list.append('第 ' + str(data_id) + ' 条数据中 ' + test_data + ' 值类型错误：' + str(type(test_field[test_data])) + ' | 应为：' + str(type(target_data)))
            else:
                fail_list.append(test_data + ' 值类型错误：' + str(type(test_field[test_data])) + ' | 应为：' + str(type(target_data)))
        elif test_field[test_data] != target_data:
            if data_id != None:
                fail_list.append('第 ' + str(data_id) + ' 条数据中 ' + test_data + ' 错误：' + str(test_field[test_data]) + ' | 应为：' + str(target_data))
            else:
                fail_list.append(test_data + ' 错误：' + str(test_field[test_data]) + ' | 应为：' + str(target_data))
    else:
        if test_field[test_data] == '' or test_field[test_data] == ' ':
            if data_id != None:
                fail_list.append('第 ' + str(data_id) + ' 条数据中 ' + test_data + ' 值为空')
            else:
                fail_list.append(test_data + ' 值为空')


def checkLinking(test_field, test_data, fail_list=[], st_code = 200, data_id=None):
    if test_data == None:
        if requests.get(test_field).status_code != st_code:
            fail_list.append('flush 链接无效')
    else:
        if data_id != None and st_code == 200:
            if test_field[test_data] != '' and test_field[test_data] != ' ':
                try:
                    if requests.get(test_field[test_data]).status_code != st_code:
                        fail_list.append('第 %s 条数据的 %s 链接无效'%(data_id, test_data))
                except:
                    fail_list.append('第 %s 条数据的 %s 链接无效' % (data_id, test_data))
            else:
                fail_list.append('第 %s 条数据的 %s 链接为空'%(data_id, test_data))
        elif data_id != None and st_code != 200:
            if test_field[test_data] != '' and test_field[test_data] != ' ':
                try:
                    if requests.head(test_field[test_data]).status_code != st_code:
                        fail_list.append('第 %s 条数据的 %s 链接无效' % (data_id, test_data))
                except:
                    fail_list.append('第 %s 条数据的 %s 链接无效' % (data_id, test_data))
            else:
                fail_list.append('第 %s 条数据的 %s 链接为空' % (data_id, test_data))
        else:
            if test_field[test_data] != '' and test_field[test_data] != ' ':
                try:
                    if requests.get(test_field[test_data]).status_code != st_code:
                        fail_list.append('数据中 %s 链接无效'%(data_id))
                except:
                    fail_list.append('数据中 %s 链接无效' % (data_id))
            else:
                fail_list.append('数据中 %s 链接为空'%(data_id))


def getFlushUrl(test_field, fail_list=[]):
    flush_data = test_field['flush']
    http_tag = flush_data.index('http')
    next_tag = flush_data.index('换一换')
    flush_url = flush_data[http_tag: next_tag - 2]
    if requests.get(flush_url).status_code != 200:
        fail_list.append('换一换中链接无效')
    return flush_url
