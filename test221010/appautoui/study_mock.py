import mock
import study_gameui

nums = [1,2,3,4]
num = 500
def send_req(num1, num2):
    return num1+num2
def mock_send_req(num3,num4):
    return 500
def spec_send():
    print("使用spec")
    return 100
if __name__ == '__main__':
    #创建mock对象
    mock_value = mock.Mock(side_effect=mock_send_req)#使用方法
    mock_value1 = mock.Mock(return_value=study_gameui.mock_test())#使用返回值:具体数据，方法，对象
    mock_value2 = mock.Mock(spec=nums)#使用返回对象
    #赋值给方法名
    send_req = mock_value
    spec_send = mock_value1
    #调用被赋值的方法
    print(send_req(1,2))
    print(spec_send())


