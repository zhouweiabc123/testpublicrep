import logging

import requests
import sys

#from test221010.conf.conf import MyConfig

sys.path.append(r"D:\A_Python\GitProjects\ServerProject\testpublicrep\test221010\test")
import pytest
import allure
import yaml
import os
import time
import allure_pytest
from test221010.log import mylog

#from test221010.conf.conf import MyConfig


#import yaml
# from ddt import data,file_data
@allure.epic("X项目")
@allure.feature("登录注册模块")
class TestLogin:
    '''
    @allure.severity("用例等级")
    BLOCKER = 'blocker'
    CRITICAL = 'critical'
    NORMAL = 'normal'
    MINOR = 'minor'
    TRIVIAL = 'trivial'
    '''
    logging.getLogger("log1")
   # configurl = MyConfig.test_url
    #configurl = 'https://isp-dev.hhygames.com'
    configurl = 'https://isp.hhygames.com'
    # index_url = 'https://isp-dev.hhycdk.com/login/index'
    index_url = 'https://isp.hhycdk.com/login/index'

    #gameId = MyConfig.gameId['73','33']
    gameId = '32'
    #根据当前时间判断使用的gameId
    ltime = time.localtime()#获取本地时间
    ftime = time.strftime("%Y-%m-%d %H:%M:%S",ltime)#格式化
    YMD = time.strftime("%Y-%m-%d",ltime)#拿到当前年月日
    if ftime > f"{YMD} 12:00:00":
        gameId = '73' # 73
    same_gameId = 107
    tourtoken = None

    #时间在10:30:00到18:00:00之间使用dev环境，gameId使用'73'
    dev_start_time = f"{YMD} 10:30:00"
    dev_end_time = f"{YMD} 18:00:00"
    if dev_start_time<ftime<dev_end_time:
        configurl = 'https://isp-dev.hhygames.com'
        index_url = 'https://isp-dev.hhycdk.com/login/index'
        gameId = '73'
    #日志记录configurl，index_url，gameId
    mylog.mylog.info(f"configurl：{configurl}，index_url：{index_url}，gameId：{gameId}")
    def yml_load(self,file):
        with open(file,'r',encoding='utf-8') as f:
            data = yaml.full_load(f)
        print(data)
        return data
       # yaml.load(open('test221010/test/login.yml', 'r'), Loader=yaml.Loader)
    #登录
    #用例级别,severity()
    # BLOCKER = 'blocker'
    # CRITICAL = 'critical'
    # NORMAL = 'normal'
    # MINOR = 'minor'
    # TRIVIAL = 'trivial'
    @pytest.mark.parametrize('data', yaml.load_all(open(r'D:\A_Python\GitProjects\ServerProject\testpublicrep\test221010\test/yml/login.yml','r',encoding='utf-8')))
    @allure.story('密码正确，登录成功')
    @allure.severity('critical')
    def test_01_login(self,data):

        #组装数据
        #mylog.mylog.info('开始接口测试')
        with allure.step("添加请求头"):
            header = {'User-Agent':"Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"}
        #发送请求
        with allure.step("发送请求"):
            res = requests.post(url=self.configurl+data[0]['api'],json={
                "account": data[0]['user'],
                "password": data[0]['password'],
                "gameId": self.gameId,
                "apothecary_inexcusable_willful": None,
                "fast_shelve": None,
                "rhyme_systolic": None
            },headers=header)
        #print(res.status_code)
        response =res.json()
        print(response)
        #print(res.raw)
        #断言
        with allure.step('断言'):
            assert response['msg'] == ''
        print(data)
        #mylog.mylog.info('断言完成，登录接口测试结束')
        # assert 1 == 2
    #通过参数化，结合yaml文件获取数据并使用
    @allure.story("多组数据登录失败")
    @pytest.mark.parametrize('data1', yaml.load_all(open(r'D:\A_Python\GitProjects\ServerProject\testpublicrep\test221010\test/yml/erroruser.yml','r',encoding='utf-8')), )
    def test_02_loginfail(self,data1):
        # 组装数据
        with allure.step("添加请求头"):
            header = {
                'User-Agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"}
        # 发送请求
        with allure.step("发送请求"):
            res = requests.post(url=self.configurl+data1[0]['api'], json={
                "account": data1[0]['user'],
                "password": data1[0]['password'],
                "gameId": self.gameId,
                "apothecary_inexcusable_willful": None,
                "fast_shelve": None,
                "rhyme_systolic": None
            }, headers=header)
        with allure.step("发送请求"):
            res1 = requests.post(url=self.configurl+data1[1]['api'], json={
                "account": data1[1]['user'],
                "password": data1[1]['password'],
                "gameId": self.gameId,
                "apothecary_inexcusable_willful": None,
                "fast_shelve": None,
                "rhyme_systolic": None
            }, headers=header)
        # print(res.status_code)
        response1 = res.json()
        response2 = res1.json()
        print(data1)
        print(response1)
        print(response2)
        #print(response)
        # print(res.raw)
        # 断言
        with allure.step('断言'):
            assert response1['msg'] == "账号密码错误"
            assert response2['msg'] == "账号密码错误"
    #发送游客登录请求并获取返回数据
    @allure.feature('游客注册登录模块')
    @pytest.fixture(scope='session')
    def touristdata(self):
        tourdata = yaml.full_load(open(r'D:\A_Python\GitProjects\ServerProject\testpublicrep\test221010\test/yml/touristcreate.yml', 'r', encoding='utf-8'))
        header = {'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'}
        #"gameId": tourdata[0]["gameId"]
        res = requests.post(url=self.configurl+tourdata[0]['api'],json={
            "gameId": self.gameId,
            "launchCode": "",
            "launchType": "h5",
            "apothecary_inexcusable_willful": None,
            "fast_shelve": None,
            "rhyme_systolic": None
        },headers=header)#'/sdkCreate/touristCreate'
        data = res.json()
        #self.tourtoken = data['data']['token']
        data['tour'] = tourdata
        return data
    #判断游客是否生成成功
    @allure.story('生成游客账号成功')
    def test_03_tourist_register(self,touristdata):
        with allure.step('查看游客账号'):
            print('输出游客')
        print(touristdata)
        assert touristdata['data']['isRegister'] == True
    #拿到生成的正确游客账号，去登录
    @allure.story("游客登录成功")
    @pytest.mark.parametrize('data', yaml.load_all(open(r'D:\A_Python\GitProjects\ServerProject\testpublicrep\test221010\test/yml/touristlogin.yml','r',encoding='utf-8')))
    def test_04_tourist_login(self,touristdata,data):
        # 组装数据
        with allure.step("添加请求头"):
            header = {
                'User-Agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"}
        # 发送请求
        with allure.step("发送请求"):
            res = requests.post(url=self.configurl + data[0]['api'], json={
                "account": touristdata['data']['account'],
                "password": touristdata['data']['password'],
                "gameId": self.gameId,
                "apothecary_inexcusable_willful": None,
                "fast_shelve": None,
                "rhyme_systolic": None
            }, headers=header)
        # print(res.status_code)
        response = res.json()
        print(response)
        #self.tourtoken = response['data']['token']

        # print(res.raw)
        # 断言
        with allure.step('断言'):
            assert response['msg'] == ''
        #拿token
        print(touristdata)
        return response['data']['token']

    #token获取
    @pytest.fixture()
    def get_token(self,touristdata):
        # 组装数据
        with allure.step("添加请求头"):
            header = {
                'User-Agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"}
        # 发送请求
        with allure.step("发送请求"):
            res = requests.post(url=self.configurl+'/sdkLogin/playerAccount', json={
                "account": touristdata['data']['account'],
                "password": touristdata['data']['password'],
                "gameId":self.gameId,
                "apothecary_inexcusable_willful": None,
                "fast_shelve": None,
                "rhyme_systolic": None
            }, headers=header)
        # print(res.status_code)
        response = res.json()
        return response['data']['token']



    #登录游戏，实名认证开启，未实名认证需实名认证
    @allure.story("实名认证开启，未实名认证需实名认证成功")
    @pytest.mark.parametrize('realdata', yaml.load_all(open(r'D:\A_Python\GitProjects\ServerProject\testpublicrep\test221010\test/yml/touristreal.yml', 'r', encoding='utf-8')))
    def test_05_tourist_realuser(self,realdata,get_token):
        #组装数据
        header = {'token':get_token,'User-Agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"}
        #发送请求
        res = requests.post(url=self.configurl+realdata[0]['api'],json={
        "realName": realdata[0]["realName"],
        "idCard": realdata[0]["idCard"],
        "apothecary_inexcusable_willful": None,
        "fast_shelve": None,
        "rhyme_systolic": None
        },headers=header)
        response = res.json()
        mylog.mylog.info(response)
        #断言 ['data']['indulgeCd']
        indulgeCd = response['data']['indulgeCd']
        realNameResult = response['data']['realNameResult']
        assert indulgeCd == 0 or realNameResult == 1
        #assert response == 0
        print(response)

    @allure.story("修改密码成功")
    @pytest.mark.parametrize('pwddata', yaml.load_all(open(r"D:\A_Python\GitProjects\ServerProject\testpublicrep\test221010\test/yml/newpwd.yml", "r", encoding="utf-8")))
    def test_06_tourist_setpwd(self,pwddata,get_token):
        with allure.step("获取要修改的账号token"):
            print("拿到token备用")
            # token = self.get_token
        # 组装数据
        header = {"token":get_token,"User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"}
        # 发送请求
        res = requests.post(url=self.configurl+pwddata[0]['api'],json={'newPassword':pwddata[0]['newPassword']},headers=header)
        # 断言
        response = res.json()
        print(response)
        assert response['code'] == 0

    new_token = None

    @allure.story("修改密码后使用新密码重新登录成功")
    @pytest.mark.parametrize('newpwds', yaml.load_all(open(r'D:\A_Python\GitProjects\ServerProject\testpublicrep\test221010\test/yml/newpwd.yml','r',encoding='utf-8')))
    def test_07_newpwdLogin_tourist(self,touristdata,newpwds):
        # 组装数据
        header = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"}
        # 发送请求，拿到修改后的密码
        #ewpwds = yaml.full_load(open(r'./yml/newpwd.yml'))
        print(newpwds)
        newpassword = newpwds[0]['newPassword']
        print(newpassword)
        with allure.step("发送请求"):
            res = requests.post(url=self.configurl +newpwds[0]['logapi'] , json={
                "account": touristdata['data']['account'],
                #"password": touristdata['data']['password'],touristdata['data']['password']
                #"password": touristdata['data']['password'],#原密码
                "password": newpassword,#修改后的密码
                "gameId": self.gameId,
                "apothecary_inexcusable_willful": None,
                "fast_shelve": None,
                "rhyme_systolic": None
            }, headers=header)
        # 断言
        response = res.json()
        self.new_token = 'token'
        print(response)
        assert response['code'] == 0

    #@pytest.mark.parametrize('newpwds',yaml.load_all(open(r'./yml/newpwd.yml')))
    @pytest.fixture()
    def new_tourist_data(self, touristdata):
        newpwds= yaml.full_load(open(r'D:\A_Python\GitProjects\ServerProject\testpublicrep\test221010\test/yml/newpwd.yml','r',encoding='utf-8'))
        # 组装数据
        header = {
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"}
        # 发送请求，拿到修改后的密码
        # ewpwds = yaml.full_load(open(r'./yml/newpwd.yml'))
        print(newpwds)
        newpassword = newpwds[0]['newPassword']
        print(newpassword)
        with allure.step("发送请求"):
            res = requests.post(url=self.configurl + '/sdkLogin/playerAccount', json={
                "account": touristdata['data']['account'],
                # "password": touristdata['data']['password'],touristdata['data']['password']
                # "password": touristdata['data']['password'],#原密码
                "password": newpassword,  # 修改后的密码
                "gameId": self.gameId,
                "apothecary_inexcusable_willful": None,
                "fast_shelve": None,
                "rhyme_systolic": None
            }, headers=header)
        # 断言
        response = res.json()
        print(response)
        return response
        #assert response['code'] == 0


    @allure.story("修改密码后使用原密码重新登录失败")
    def test_08_oldpwdLoginFail_tourist(self, touristdata):
        # 组装数据
        header = {
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"}
        # 发送请求，拿到修改后的密码
        # ewpwds = yaml.full_load(open(r'./yml/newpwd.yml'))
        with allure.step("发送请求"):
            res = requests.post(url=self.configurl + '/sdkLogin/playerAccount', json={
                "account": touristdata['data']['account'],
                "password": touristdata['data']['password'],  # 原密码
                # "password": newpassword,#修改后的密码
                "gameId": self.gameId,
                "apothecary_inexcusable_willful": None,
                "fast_shelve": None,
                "rhyme_systolic": None
            }, headers=header)
        # 断言
        response = res.json()
        print(response)
        assert response['msg'] == '账号密码错误'
    @allure.story("用户在游戏里面反馈意见")
    #@pytest.mark.parametrize('newtoken',new_token)
    def test_09_sendreason_success(self,new_tourist_data):
        newtoken = new_tourist_data['data']['token']
        # 组装数据
        header = {
            'Content - Type': 'application / json;charset = UTF - 8',
            "token":newtoken,
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"}
        # 发送请求，拿到修改后的密码
        # ewpwds = yaml.full_load(open(r'./yml/newpwd.yml'))
        with allure.step("发送请求"):
            res = requests.post(url=self.configurl + '/info/feedback', json={'content':"用户反馈了一条意见"}, headers=header)
        # 断言
        response = res.json()
        print(response)
        assert 0 == response['code']
    #获取当前时间戳
    @pytest.fixture()
    def mk_time(self):
        ltime = time.localtime()
        mktime= time.mktime(ltime)
        return int(mktime)
    #获取支付校验参数集
    @pytest.fixture()
    def pay_data(self):
        paydata = yaml.full_load(open(r'D:\A_Python\GitProjects\ServerProject\testpublicrep\test221010\test/yml/paychekdata.yml','r',encoding='utf-8'))
        return paydata
    #获取年龄参数
    @pytest.fixture()
    def get_age(self,new_tourist_data):
        '''
        获取年龄
        :param new_tourist_data:
        :return:
        '''
        data = yaml.full_load(open(r"D:\A_Python\GitProjects\ServerProject\testpublicrep\test221010\test/yml/realNameSwitchs.yml",'r',encoding='utf-8'))
        api = data[0]['api']
        newtoken = new_tourist_data['data']['token']
        header = {
            'Content - Type': 'application / json;charset = UTF - 8',
            "token": newtoken,
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"}
        res = requests.post(url=self.configurl+api,headers=header)
        response = res.json()
        print(response)
        return response['data']['age']
    #创建订单的固定参数
    @pytest.fixture()
    def create_data(self):
        data = yaml.full_load(r"D:\A_Python\GitProjects\ServerProject\testpublicrep\test221010\test/yml/create.yml","r",encodings="utf-8")

    #获取openId
    @pytest.fixture()
    def get_openId(self,get_age,new_tourist_data,mk_time):
        data  = yaml.full_load(open(r"D:\A_Python\GitProjects\ServerProject\testpublicrep\test221010\test/yml/index.yml","r",encoding="utf-8"))
        playerId = new_tourist_data['data']['playerId']#获取playerId
        sign = new_tourist_data['data']['sign']#获取sign
        get_age = get_age+10 #未成年会失败，所以给年龄加10
        get_age = str(get_age)
        header = {
            'Content - Type': 'application / json;charset = UTF - 8',
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"}
        param_json = {
            'playerId': playerId,
            'timestamp': str(mk_time),
            'age': get_age,
            "launchCode": "",
            'gameId': self.same_gameId,
            'sign': sign,
            'tsKey': data[0]['tsKey'],
            'snKey': data[0]['snKey'],
            'zoneKey': data[0]['zoneKey']
        }
        js = {
                "playerId": "11ed7476679da1225254009c2f09ae53",
                "timestamp": "1670832684",
                "age": "23",
                "launchCode": "",
                "sign": "2F4485A04246E4F494FC4B0555174E76",
                "snKey": "h0413",
                "zoneKey": "frx_fzml",
                "tsKey": "fangZhouGH",
                "gameId": 107
                }
        '''{
    "playerId": "11ed7476679da1225254009c2f09ae53",
    "timestamp": "1670832684",
    "age": "23",
    "launchCode": "",
    "sign": "2F4485A04246E4F494FC4B0555174E76",
    "snKey": "h0413",
    "zoneKey": "frx_fzml",
    "tsKey": "fangZhouGH",
    "gameId": 107
}'''
        res = requests.post(url=self.index_url, json=param_json, headers=header)#url=data[0]["api"]
        response = res.json()
        i = 1
        # requests 请求返回的数据是错误的，继续请求，知道正确为止
        if response['code'] == 1:
            while(i<51):
                mylog.mylog.info(f'尝试循环获取open_Id第{i}次')
                res  = requests.post(url=data[0]["api"], json=param_json, headers=header)
                response = res.json()
                i+=1
                if response['code'] == 0:
                    mylog.mylog.info(f'第{i}次获取open_Id成功')
                    break;
                elif i == 50:
                    mylog.mylog.info('获取失败，将不执行订单创建接口！')
        elif response['code'] == 0:
            mylog.mylog.info('获取open_Id成功')

        print(response)
        #assert response == ''
        if response['code'] == 0:
            index_data = response['data']
            return index_data
        return 1 #表示获取open_Id失败

    #通过open_Id查询角色信息
    #@pytest.fixture()
    def test_50_get_userInfo(self,get_openId,mk_time):
        if get_openId == 1:
            print(get_openId)
            assert get_openId ==2
            return 0
        header = {'Content - Type': 'application / json;charset = UTF - 8',
                  "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"}
        #https://h5-dev.hhygames.com/dfs/h5SDK/?gameId=73#
        res = requests.post(url=self.configurl+'/getRoleInfo',json={'openId':get_openId['openId'],'tiemstamp':str(mk_time),'sign':get_openId['sign']},headers=header)
        print(res)
        assert res.json() == 99
        return res.json()

    @allure.story("18岁成年，支付校验通过")
    @pytest.mark.parametrize('paydata',yaml.load_all(open(r'D:\A_Python\GitProjects\ServerProject\testpublicrep\test221010\test/yml/paychekdata.yml','r',encoding='utf-8')))
    def test_10_payChek_success(self,new_tourist_data,paydata):
        #获取当前时间
        print("当前时间string形式：",time.ctime())
        print(time.localtime())
        ltime = time.localtime() #tm_year=2022, tm_mon=12, tm_mday=8, tm_hour=10, tm_min=1, tm_sec=21, tm_wday=3, tm_yday=342, tm_isdst=0
        #格式化时间
        print("格式化后的时间：",time.strftime('%Y-%m-%d %H:%M:%S',ltime))
        #转化成时间戳
        mk_time = int(time.mktime(ltime))
        print("时间戳...",mk_time)
        print("支付参数...")

        newtoken = new_tourist_data['data']['token']
        # 组装数据
        header = {
            'Content - Type': 'application / json;charset = UTF - 8',
            "token": newtoken,
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"}
        # 发送请求，拿到修改后的密码
        # ewpwds = yaml.full_load(open(r'./yml/newpwd.yml'))
        with allure.step("发送请求"):
            res = requests.post(url=self.configurl+paydata[0]['api'],json={
                'accountId':new_tourist_data['data']['playerId'],
                'age':paydata[0]['age'],
                'amount':paydata[0]['amount'],
                'gameId':self.gameId
            },headers=header)
        # 断言
        response = res.json()
        print(response)
        if paydata[0]['indulge'] == 1:
            #防沉迷开启
            assert response['code'] == 0
        elif paydata[0]['indulge'] == 0:
            #防沉迷关闭
            pass


    @allure.story("16到18岁充值校验")
    def test_11_payCheck_big_age(self,pay_data,new_tourist_data):
        newtoken = new_tourist_data['data']['token']
        header ={
            'Content - Type': 'application / json;charset = UTF - 8',
            "token": newtoken,
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"}
        res = requests.post(url=self.configurl+pay_data[0]['api'],json={
                'accountId':new_tourist_data['data']['playerId'],
                'age':pay_data[0]['big_age'],
                'amount':pay_data[0]['amount'],
                'gameId':self.gameId
            },headers=header)
        response = res.json()
        print(response)
        if pay_data[0]['indulge'] == 1:
            #防沉迷开启
            assert pay_data[0]['except_bigstr'] in response['msg']
        elif pay_data[0]['indulge'] == 0:
            #防沉迷关闭,不校验
            assert response['msg'] == ''


    @allure.story("8到15岁充值校验")
    def test_12_payCheck_midl_age(self, pay_data, new_tourist_data):
        newtoken = new_tourist_data['data']['token']
        header = {
            'Content - Type': 'application / json;charset = UTF - 8',
            "token": newtoken,
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"}
        res = requests.post(url=self.configurl + pay_data[0]['api'], json={
            'accountId': new_tourist_data['data']['playerId'],
            'age': pay_data[0]['midl_age'],
            'amount': pay_data[0]['amount'],
            'gameId': self.gameId
        }, headers=header)
        response = res.json()
        print(response)
        if pay_data[0]['indulge'] == 1:
            # 防沉迷开启
            assert pay_data[0]['except_midlstr'] in response['msg']
        elif pay_data[0]['indulge'] == 0:
            # 防沉迷关闭,不校验
            pass

    @allure.story("8岁以下充值校验")
    def test_13_payCheck_small_age(self, pay_data, new_tourist_data):
        newtoken = new_tourist_data['data']['token']
        header = {
            'Content - Type': 'application / json;charset = UTF - 8',
            "token": newtoken,
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"}
        res = requests.post(url=self.configurl + pay_data[0]['api'], json={
            'accountId': new_tourist_data['data']['playerId'],
            'age': pay_data[0]['small_age'],
            'amount': pay_data[0]['amount'],
            'gameId': self.gameId
        }, headers=header)
        response = res.json()
        print(response)
        if pay_data[0]['indulge'] == 1:
            # 防沉迷开启
            assert pay_data[0]['except_smallstr'] in response['msg']
        elif pay_data[0]['indulge'] == 0:
            # 防沉迷关闭,不校验
            pass

    @allure.story("创建订单，如果没获取到open_Id就跳过")
    #@pytest.mark.skipif()
    def test_14_create(self,get_openId):
        '''
        还未完成创建订单接口，获取openId不稳定
        '''
        assert 2 == get_openId


    @allure.feature("未完成模块")
    def test_05_tourist_loginfail(self,pay_data):
        #  big_age: '16'
        #  midl_age: '11'
        #  small_age: '6'
        #  amount: '19800'
        #  except_bigstr:
        #  except_midlstr: '游戏中8周岁以上未满16周岁的用户'
        assert 1==pay_data

    @allure.story("失败的用例")
    @pytest.fixture()
    def test_02_register(self):
        with allure.step("输出数字"):
            print(333)

        with allure.step("输出地址"):
            path = os.path.join(os.path.abspath(__file__), 'yml/login.yml')
            print(path)
        assert 3 == 2
    @pytest.fixture(params=[1,2,3,],ids=['1排第一','2排第二','3排第三'])
    def logindata(self,request):
        num = request.param
        print(f"== 账号是：{num} ==")
        return num
    @pytest.fixture(scope="module")#执行前置和后置
    def log(self):
        print('日志前')
        yield
        print('日志后')

    #使用fixtured的参数
    @allure.feature('参数传入模块')
    def test_04_usedata(self,logindata):
        print(logindata)
        assert logindata < 1
    @allure.story("可能会发生错误的用例也要执行")
    #@pytest.xfail("发生了点错误")
    def test_05_jump(self):
        assert 1==1
    @allure.feature("订单模块")
    @allure.story("尝试创建正确订单，创建成功")
    def test_15_creatorder(self,new_tourist_data):
        newtoken=new_tourist_data["data"]["token"]
        assert 1==new_tourist_data
        mylog.mylog.info(new_tourist_data)
        #组装数据
        header = {
            'Content - Type': 'application / json;charset = UTF - 8',
            "token": newtoken,
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"}

        #发送请求
        req=requests.get(url=self.configurl+"/switchs/loginSwitch",json={})
        #断言

    @pytest.fixture(params=['32','33','37','79','80','85','96'],ids=["32除妖","33请问","37斗魂","79幻刃录","80斗争","85三国","96直播包"])
    def gameids_data(self,request):
        gid=request.param
        return gid
    @allure.feature("登录注册开关控制模块")
    @allure.story("登录开关查询控制")
    @allure.severity("normal")
    #@pytest.mark.parametrize('login_swich_data',yml_load(open()))
    def test_16_loginMethodGet(self,gameids_data):
        '''
        查询游戏登录注册方法是否正常，断言code
        '''
        #组装数据
        header = {
            'Content - Type': 'application / json;charset = UTF - 8',
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"}
        data={"gameId": gameids_data,"apothecary_inexcusable_willful": None,"fast_shelve": None,"rhyme_systolic": None}
        # 发送请求
        with allure.step("发送请求"):
            req = requests.post(url=self.configurl + "/switchs/loginSwitch", json=data,headers=header)
            response=req.json()
            print(response)

        #断言
        with allure.step("断言"):
            assert response["code"] == 0

if __name__ == '__main__':
    # lg = TestLogin()
    # lg.test_01_login
    #mylog.mylog.info("1")

    print(123)
    #path = os.path.join(os.path.abspath(__file__), 'yml/login.yml')
    #print(path)
    #tourdata = yaml.full_load(open(r'/test221010/test/yml/touristcreate.yml', 'r', encoding='utf-8'))
    #print(tourdata)

    # 执行
    # pytest .\test221010\test\test_LoginApi.py -s -q --alluredir=./result/
    #生成测试报告
    #allure generate ./result/ -o ./report/ --clean
    #打开报告
    #allure server ./reprot/index.html


