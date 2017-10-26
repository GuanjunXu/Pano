import unittest
import requests
import util as u

proto = 'http'
host = '220.181.1.151'
port = '8999'
body = 'lekan/panolanding_json.so'
params = {
    'terminalApplication': 'supersearch',
    'token': '',
    'coor': 'bd09ll',
    'card_id': '203-521-522-523-502-506-210-211-503-504-505-702-515-901-903',
    'imei': '868897023472871',
    'ad_parm': '',
    'terminalBrand': 'LeEco',
    'video_history': '',
    'sales_area': 'CN',
    'lang': 'zh_cn',
    'version': '3.0.3',
    'num': '30',
    'terminalSeries': 'Le_X620_whole-netcom',
    'pcode': '160110000',
    'music_history': '',
    'weather_city_code': '01010101',
    'longitude': '116.49819801016548',
    'mac': '847303E7DCA0',
    'bsChannel': 'letv_supersearch',
    'from': 'mobile_super18',
    'ad_session': '834a8af69e6e4ff89a4deaf728bad3f4-1502705471771',
    'module_order_enable': '1',
    'user_setting_country': 'CN',
    'latitude': '39.94046478007413',
    'uid': '',
    'wcode': 'cn',
    'devId': '868897023472899',
    'districtid': '9'
}

paramstring = ''
for k in params.keys():
    kv = k + '=' + params[k]
    paramstring += kv + '&'
test_url = proto + '://' + host + ':' + port + '/' + body + '?' + paramstring[:-1]
r = requests.get(test_url)
content = r.json()
all_cards = u.getAllCards(content, "data:home_page_module_order")


class PanoEachCard(unittest.TestCase):
    def setUp(self):
        super(PanoEachCard, self).setUp()
        self.fail_list = []

    def tearDown(self):
        super(PanoEachCard, self).tearDown()
        if len(self.fail_list) != 0:
            for fail in self.fail_list:
                print(fail)
        else:
            print('所有测试点验证通过')
        print('* - * - * - * - * - * - * - * - ')

    def testGameCard(self):
        print('测试模块：您的好友正在玩')
        test_card = u.getDataByText(all_cards, '您的好友正在玩')
        if test_card is not None:
            u.checkField(test_card, 'template', 10011, self.fail_list)
            u.checkField(test_card, 'card_id', 521, self.fail_list)
            fls_url = u.getFlushUrl(test_card, self.fail_list)
            u.checkLinking(fls_url, test_data=None, fail_list=self.fail_list)
            game_flush = requests.get(fls_url).json()['data']['records']
            if len(game_flush) < 1:
                self.fail_list.append('换一换中数据为空')
            else:
                self.fail_list.append('>>> 换一换 records 内各条目检查：')
                len_one = len(self.fail_list)
                i = 0
                for rec in game_flush:
                    u.checkLinking(rec, 'image', self.fail_list, data_id=i)
                    u.checkLinking(rec, 'action', self.fail_list, data_id=i)
                    u.checkLinking(rec, 'download_url', self.fail_list, st_code=302, data_id=i)
                    u.checkField(rec, 'template', 36, self.fail_list)
                    i += 1
                if len(self.fail_list) == len_one:
                    self.fail_list.pop()
            if len(test_card['records']) > 0:
                self.fail_list.append('>>> records 内各条目检查：')
                len_one = len(self.fail_list)
                i = 0
                for game in test_card['records']:
                    u.checkField(game, 'template', 36, self.fail_list)
                    u.checkLinking(game, 'image', self.fail_list, data_id=i)
                    u.checkLinking(game, 'action', self.fail_list, data_id=i)
                    u.checkLinking(game, 'download_url', self.fail_list, st_code=302, data_id=i)
                    i += 1
                if len(self.fail_list) == len_one:
                    self.fail_list.pop()
            else:
                self.fail_list.append('游戏数量缺少：%s' % len(test_card['records']))
        else:
            self.fail_list.append('卡片未找到')

    def testRecommend(self):
        print('测试模块：您周围的人正在使用')
        test_card = u.getDataByText(all_cards, '您周围的人正在使用')
        if test_card is not None:
            u.checkField(test_card, 'template', 10012, self.fail_list)
            u.checkField(test_card, 'card_id', 523, self.fail_list)
            fls_url = u.getFlushUrl(test_card, self.fail_list)
            u.checkLinking(fls_url, test_data=None, fail_list=self.fail_list)
            game_flush = requests.get(fls_url).json()['data']['records']
            if len(game_flush) < 1:
                self.fail_list.append('换一换中数据为空')
            else:
                self.fail_list.append('>>> 换一换 records 内各条目检查：')
                len_one = len(self.fail_list)
                i = 0
                for rec in game_flush:
                    u.checkLinking(rec, 'image', self.fail_list, data_id=i)
                    u.checkLinking(rec, 'action', self.fail_list, data_id=i)
                    u.checkLinking(rec, 'download_url', self.fail_list, st_code=302, data_id=i)
                    u.checkField(rec, 'template', 37, self.fail_list)
                    i += 1
                if len(self.fail_list) == len_one:
                    self.fail_list.pop()
            if not len(test_card['records']) < 1:
                self.fail_list.append('>>> records 内各条目检查：')
                len_one = len(self.fail_list)
                i = 0
                for game in test_card['records']:
                    u.checkField(game, 'template', 37, self.fail_list)
                    u.checkLinking(game, 'image', self.fail_list, data_id=i)
                    u.checkLinking(game, 'action', self.fail_list, data_id=i)
                    u.checkLinking(game, 'download_url', self.fail_list, st_code=302, data_id=i)
                    i += 1
                if len(self.fail_list) == len_one:
                    self.fail_list.pop()
            else:
                self.fail_list.append('应用数量缺少：%s' % len(test_card['records']))
        else:
            self.fail_list.append('卡片未找到')

    def testCommonUse(self):
        print('测试模块：常用')
        test_card = u.getDataByText(all_cards, '常用')
        if test_card is not None:
            u.checkField(test_card, 'template', 10009, self.fail_list)
            u.checkField(test_card, 'module_name', 'common_use', self.fail_list)
        else:
            self.fail_list.append('卡片未找到')

    def testNearbyService(self):
        print('测试模块：附近服务')
        test_card = u.getDataByText(all_cards, '附近服务')
        if test_card is not None:
            u.checkField(test_card, 'template', 10003, self.fail_list)
            u.checkField(test_card, 'card_id', 506, self.fail_list)
            services = test_card['records']
            if len(services) == 4:
                i = 0
                for service in services:
                    u.checkField(service, 'dataType', 31, self.fail_list)
                    u.checkField(service, 'card_id', '506', self.fail_list)
                    u.checkField(service, 'template', 4, self.fail_list)
                    u.checkLinking(service, 'image', self.fail_list, data_id=i)
                    if service['content'] == '找工作':
                        u.checkField(service, 'index', 0, self.fail_list)
                        u.checkField(service, 'service_category_id', 1, self.fail_list)
                        u.checkField(service, 'sub_module', '5', self.fail_list)
                    elif service['content'] == '爱生活':
                        u.checkField(service, 'index', 1, self.fail_list)
                        u.checkField(service, 'service_category_id', 2, self.fail_list)
                        u.checkField(service, 'sub_module', '9', self.fail_list)
                    elif service['content'] == '找房子':
                        u.checkField(service, 'index', 2, self.fail_list)
                        u.checkField(service, 'service_category_id', 3, self.fail_list)
                        u.checkField(service, 'sub_module', '7', self.fail_list)
                    elif service['content'] == '读好书':
                        u.checkField(service, 'index', 3, self.fail_list)
                        u.checkField(service, 'service_category_id', 4, self.fail_list)
                        u.checkField(service, 'sub_module', '8', self.fail_list)
                    elif service['content'] == '二手市场':
                        u.checkField(service, 'index', 3, self.fail_list)
                        u.checkField(service, 'service_category_id', 4, self.fail_list)
                        u.checkField(service, 'sub_module', '8', self.fail_list)
                i += 1
            else:
                self.fail_list.append('附近服务内无数据')
        else:
            self.fail_list.append('卡片未找到')

    def testWeibo(self):
        print('测试模块：微博')
        test_card = u.getDataByText(all_cards, '微博')
        if test_card is not None:
            u.checkField(test_card, 'template', 10000, self.fail_list)
            u.checkField(test_card, 'union_card_id', "503-504-505", self.fail_list)
            fls_url = u.getFlushUrl(test_card, self.fail_list)
            u.checkLinking(fls_url, test_data=None, fail_list=self.fail_list)
            for tab in test_card['records']:
                if tab['name'] == '热门微博':
                    u.checkField(tab, 'card_id', 503, self.fail_list)
                    i = 0
                    for cont in tab['records']:
                        u.checkField(cont, 'template', 5, self.fail_list, i)
                        u.checkField(cont, 'content', '', self.fail_list, i)
                        u.checkField(cont, 'title', '', self.fail_list, i)
                        u.checkLinking(cont, 'image', self.fail_list, data_id=i)
                        i += 1
                elif tab['name'] == '热门搜索':
                    u.checkField(tab, 'card_id', 505, self.fail_list)
                    i = 0
                    for cont in tab['records']:
                        u.checkField(cont, 'template', 19, self.fail_list, i)
                        u.checkField(cont, 'content', '', self.fail_list, i)
                        i += 1
                elif tab['name'] == '热门话题':
                    u.checkField(tab, 'card_id', 504, self.fail_list)
                    i = 0
                    for cont in tab['records']:
                        u.checkField(cont, 'template', 20, self.fail_list, i)
                        u.checkField(cont, 'content', '', self.fail_list, i)
                        u.checkField(cont, 'title', '', self.fail_list, i)
                        u.checkLinking(cont, 'image', self.fail_list, data_id=i)
                        i += 1
        else:
            self.fail_list.append('卡片未找到')

    def testAudio(self):
        print('测试模块：我的爱听')
        test_card = u.getDataByText(all_cards, '我的爱听')
        if test_card is not None:
            u.checkField(test_card, 'template', 10003, self.fail_list)
            u.checkField(test_card, 'card_id', 203, self.fail_list)
            fls_url = u.getFlushUrl(test_card, self.fail_list)
            u.checkLinking(fls_url, test_data=None, fail_list=self.fail_list)
            i = 0
            for music in test_card['records']:
                u.checkField(music, 'template', 12, self.fail_list, i)
                u.checkField(music, 'content', '', self.fail_list, i)
                u.checkField(music, 'title', '', self.fail_list, i)
                u.checkLinking(music, 'image', self.fail_list, data_id=i)
                i += 1
        else:
            self.fail_list.append('卡片未找到')

    def testWeather(self):
        print('测试模块：天气')
        test_card = u.getDataByText(all_cards, '天气')
        if test_card is not None:
            u.checkField(test_card, 'template', 10, self.fail_list)
            u.checkField(test_card, 'card_id', 502, self.fail_list)
            u.checkField(test_card, 'weather_city_code', '', self.fail_list)
            u.checkField(test_card, 'city', '', self.fail_list)
            u.checkField(test_card, 'name', '', self.fail_list)
        else:
            self.fail_list.append('卡片未找到')

    def testInterestCover(self):
        print('测试模块：大家都在搜')
        test_card = u.getDataByText(all_cards, '大家都在搜')
        if test_card is not None:
            u.checkField(test_card, 'template', 10003, self.fail_list)
            u.checkField(test_card, 'card_id', 702, self.fail_list)
            i = 0
            for interest in test_card['records']:
                u.checkField(interest, 'template', 19, self.fail_list, i)
                u.checkField(interest, 'content', '', self.fail_list, i)
                i += 1
        else:
            self.fail_list.append('卡片未找到')

    def testSets(self):
        print('测试模块：个性化设置')
        test_card = u.getDataByText(all_cards, '个性化设置')
        if test_card is not None:
            u.checkField(test_card, 'template', 24, self.fail_list)
            u.checkField(test_card, 'card_id', 515, self.fail_list)
            u.checkField(test_card, 'content', '想要更加贴心的万象？', self.fail_list)
            u.checkField(test_card, 'info', '进入个性化设置', self.fail_list)
        else:
            self.fail_list.append('卡片未找到')

    def testPull(self):
        print('测试模块：下拉框')
        test_card = u.getDataByText(all_cards, '下拉框')
        if test_card is not None:
            u.checkField(test_card, 'template', 34, self.fail_list)
            u.checkField(test_card, 'card_id', 905, self.fail_list)
            u.checkLinking(test_card, 'image', self.fail_list)
        else:
            self.fail_list.append('卡片未找到')

    def testSuspension(self):
        print('测试模块：悬浮框')
        test_card = u.getDataByText(all_cards, '悬浮框')
        if test_card is not None:
            u.checkField(test_card, 'template', 35, self.fail_list)
            u.checkField(test_card, 'card_id', 904, self.fail_list)
            u.checkLinking(test_card, 'image', self.fail_list)
            u.checkLinking(test_card, 'action', self.fail_list)
            u.checkField(test_card, 'hidetime', 1, self.fail_list)
            u.checkField(test_card, 'hour', '', self.fail_list)
            u.checkField(test_card, 'position', 'bottom', self.fail_list)
        else:
            self.fail_list.append('卡片未找到')
