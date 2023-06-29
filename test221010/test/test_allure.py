import allure
import pytest
import os
import requests
import yaml
from test221010.log.mylog import mylog
@allure.feature("多参数获取不同token请求")
class TestStudyLogin:
    configurl = 'https://isp-dev.hhygames.com'
    # index_url = 'https://isp-dev.hhycdk.com/login/index'
    index_url = 'https://isp-dev.hhycdk.com/login/index'
    # gameId = MyConfig.gameId['73','33']
    gameId = '73'
    same_gameId = 107
    # 日志记录configurl，index_url，gameId
    print("下面是原先的链接和游戏ID")
    print(f"configurl：{configurl}，index_url：{index_url}，gameId：{gameId}")
    @pytest.fixture(params=["32","33","37"],ids=["32除妖","33请问","37斗魂"])
    def gameIdData(self,request):
        print(request.param)
        return request.param
    @pytest.fixture(params=['1','2','3'],ids=["a","b","c"])
    def userdatas(self,request):
        print(request.param)
        return request.param
        pass
    @allure.story("失败")
    def test_01(self,userdatas):
        print('ss')
        with allure.step("第一步"):
            print("输入密码")
            print(userdatas)

        assert userdatas == True
    @allure.story("又失败")
    def test_02(self,userdatas):
        assert 1 == 1
        assert userdatas=='2'
    @allure.story('成功了')
    def test_03(self,userdatas):
        assert 1 == 1
        assert userdatas=='2'
    @pytest.fixture()
    def test_04(self):
        print('满足条件就跳过')
        return 1
    @allure.story("与pytest结合")
    def test_05(self,test_04,gameIdData):
        print('没有任何参数')
        print("试着使用多个param，用于执行不同的用例，来得到各个游戏的参数")
        print(gameIdData)
        print(test_04)
        assert gameIdData=='32'


    @allure.feature('游客注册登录模块')
    @pytest.fixture(scope='session')
    def touristdata(self):
        tourdata = yaml.full_load(
            open(r'D:\A_Python\GitProjects\ServerProject\testpublicrep\test221010\test/yml/touristcreate.yml', 'r',
                 encoding='utf-8'))
        header = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'}
        # "gameId": tourdata[0]["gameId"]
        res = requests.post(url=self.configurl + tourdata[0]['api'], json={
            "gameId": self.gameId,
            "launchCode": "",
            "launchType": "h5",
            "apothecary_inexcusable_willful": None,
            "fast_shelve": None,
            "rhyme_systolic": None
        }, headers=header)  # '/sdkCreate/touristCreate'
        data = res.json()
        # self.tourtoken = data['data']['token']
        data['tour'] = tourdata
        return data

    # 判断游客是否生成成功
    @allure.story('生成游客账号成功')
    def test_03_tourist_register(self, touristdata):
        with allure.step('查看游客账号'):
            print('输出游客')
        print(touristdata)
        assert touristdata['data']['isRegister'] == True

    # 拿到生成的正确游客账号，去登录
    @allure.story("游客登录成功")
    @pytest.mark.parametrize('data', yaml.load_all(
        open(r'D:\A_Python\GitProjects\ServerProject\testpublicrep\test221010\test/yml/touristlogin.yml', 'r',
             encoding='utf-8')))
    def test_04_tourist_login(self, touristdata, data):
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
        # self.tourtoken = response['data']['token']

        # print(res.raw)
        # 断言
        with allure.step('断言'):
            assert response['msg'] == ''
        # 拿token
        print(touristdata)
        return response['data']['token']

    # token获取
    @pytest.fixture()
    def get_token(self, touristdata):
        # 组装数据
        with allure.step("添加请求头"):
            header = {
                'User-Agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"}
        # 发送请求
        with allure.step("发送请求"):
            res = requests.post(url=self.configurl + '/sdkLogin/playerAccount', json={
                "account": touristdata['data']['account'],
                "password": touristdata['data']['password'],
                "gameId": self.gameId,
                "apothecary_inexcusable_willful": None,
                "fast_shelve": None,
                "rhyme_systolic": None
            }, headers=header)
        # print(res.status_code)
        response = res.json()
        return response['data']['token']

    # 登录游戏，实名认证开启，未实名认证需实名认证
    @allure.story("实名认证开启，未实名认证需实名认证成功")
    @pytest.mark.parametrize('realdata', yaml.load_all(
        open(r'D:\A_Python\GitProjects\ServerProject\testpublicrep\test221010\test/yml/touristreal.yml', 'r',
             encoding='utf-8')))
    def test_05_tourist_realuser(self, realdata, get_token):
        # 组装数据
        header = {'token': get_token,
                  'User-Agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"}
        # 发送请求
        res = requests.post(url=self.configurl + realdata[0]['api'], json={
            "realName": realdata[0]["realName"],
            "idCard": realdata[0]["idCard"],
            "apothecary_inexcusable_willful": None,
            "fast_shelve": None,
            "rhyme_systolic": None
        }, headers=header)
        response = res.json()
        #mylog.mylog.info(response)
        # 断言 ['data']['indulgeCd']
        indulgeCd = response['data']['indulgeCd']
        realNameResult = response['data']['realNameResult']
        assert indulgeCd == 0 or realNameResult == 1
        # assert response == 0
        print(response)
if __name__ == '__main__':
    print("执行")
    #pytest.main(['test_allure.py','-s','-v','--alluredir','./report/allure/tmp'])
    #pytest.main(["-vs", "--html=../../report_hdc/20211011_hdc_02.html", "--self-contained-html"])
    #compytest = 'pytest ./test_allure.py --alluredir report/result'
    #commaind = 'allure generate ./report/allure/tmp'
    #os.system(compytest)
    #os.system(commaind)
    # pytest.main()