import base64

from allure_commons.utils import md5
import hashlib
import datetime

data = {
            "amount": "123",
			"areaId": "123",
			"areaName": "修神10服",
            "extension":"aHR0cDovLzE3Mi4xNi4wLjQ2OjQyMTEz","gameId":"123","gameOrderNo":"200903122817I6uF5qJ0","openId": "f6a29efc3f4ee4ff19570a246f6adf1a",
            "productDescribe":"1500仙玉","productId":"45474","productName":"1500仙玉",
			"roleId": "45940775",
			"roleName": "S710.桑炎彬",
			"roleLevel": "80",
            "timestamp":"1599107297",
			"vipGrade": 0,

}


# "goodMan":"周伟"
def sign_join(dt:dict):
    keys = dt.keys() #获取字典键集合
    keys_sort = sorted(keys,reverse=False) #按ASCII升序排列
    #为空和特别参数不参加

    print(keys_sort)
    str1 = []
    str3 = ''
    for i in range(len(keys_sort)):
        #print(keys_sort[i])
        #print(str(dt[keys_sort[i]]))

        str2 = keys_sort[i]+"="+str(dt[keys_sort[i]])#写成k=v并加入到list里面
        str1.append(str2)
    print(str1)
    str3 = '&'.join(str1).strip()#join方法组合成想要得str，strip去除左右空格
    # for i in str1:
    #     str3+=(i+"&")
    print(str3)
    return str3

def sign_encryption(data=data,game_secret="KBCagQ2s5B1pPEfk"):
    p = sign_join(data)+game_secret
    encryption_sign = md5(p).upper()
    return encryption_sign

def sign_equal(sign="04BFAD43BBDAF70451395FE907D51883",
                    game_secret = "KBCagQ2s5B1pPEfk"):
    proto = sign_join(data)+game_secret
    new_sign = md5(proto)
    print('没转大写',new_sign)
    new_sign = new_sign.upper()
    print('已转大写并输出',new_sign)
    return new_sign == sign
def sign_getdata(sign='04BFAD43BBDAF70451395FE907D51883'):
    sign_get = sign.lower()
    print(sign_get)
    a = sign_join(data)+"KBCagQ2s5B1pPEfk"
    print(sign_join(data)+"KBCagQ2s5B1pPEfk")
    md5_a=hashlib.md5(a.encode(encoding='utf-8'))
    # print(md5_a)
    print(md5_a.hexdigest().upper())
    # print(hashlib.md(sign_get))

if __name__ == '__main__':
    sign_join(data)
    print(sign_equal())
    print("==================================================")
    print(sign_encryption())
    if sign_equal():
        print("加密sign校验成功")
    else:
        print("加密校验失败")
    sign_getdata()
