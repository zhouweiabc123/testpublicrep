

import pytest
from allure_commons.utils import md5
@pytest.mark.parametrize('num1,num2',[(1,2),(2,3)])#动态入参，测试不同参数的用例执行结果
def test_param(num1,num2):

    assert num1 < 2
    assert num2 < 1

if __name__ == '__main__':
    print("开始执行测试")
    print("执行成功")
    pass