import allure
import pytest
import os
@allure.feature("111")
class LoginTest:
    @allure.story("失败")
    def test_01(self):
        print('ss')
        with allure.step("第一步"):
            print("输入密码")

        assert 1 > 2
    @allure.story("又失败")
    def test_02(self):
        assert 1 == 2
    @allure.story('成功了')
    def test_03(self):
        assert 1 == 1
    @pytest.fixture()
    def test_04(self):
        print('满足条件就跳过')
        return 1
    @allure.story("与pytest结合")
    def test_05(self,test_04):
        print('没有任何参数')
        print(test_04)
if __name__ == '__main__':
    pytest.main(['-s','-v','--alluredir','./report/allure/tmp'],'test_allure.py')
    # pytest.main(["-vs", "--html=../../report_hdc/20211011_hdc_02.html", "--self-contained-html"])
    # compytest = 'pytest test_allure.py --alluredir report/result'
    # commaind = 'allure generate ./report/result -o ./report/html'
    # os.system(compytest)
    # os.system(commaind)
    # pytest.main()