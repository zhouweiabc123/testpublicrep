import time
from itertools import count

import pandas as pd
from numpy import double


def read_excel(file,**kwargs):
    data_dict = []
    try:
        data = pd.read_excel(file,**kwargs)
        data_dict = data.to_dict('records')
    except Exception as e:
        print(e)
    finally:
        return data_dict
def total_raise(y,c,p,lr:[]):
    cy= int(c/y)
    total_list = []
    for i in range(cy):
        total = int(lr[i]*(1+p))
        lr.append(total)
        total_list.append(total)
    return total_list
def year_count(tl=[1,2,3]):
    sum = 0
    dic_year = {}
    for i in range(len(tl)):
        dic_year['第{}个三年'.format(i+1)] = tl[i]*12*3
    return dic_year
#bb为赔率，pp获胜率,money是本金，胜负基本公式
def caly(totalmoney=1000.00,fitmoney=100.00,bb=1.40,pp=0.6):
    '''
    bb为赔率，pp获胜率,totalmoney是初始本金,fitmoney是下注金额，lastmoney为余下本金
    f为本金投注比例，hp是可获赔金额
    1.4 3.4 6.4
    '''
    pb=pp*(bb+1)
    f = (pb-1)/bb
    f = f.__round__(2) #计算出投注比例
    tz = totalmoney*f  #本轮投注金额
    hp = tz*bb         #本轮获胜赔付奖金
    win_money = hp-tz  #本轮获胜净奖金
    win_money = win_money.__round__(2)
    lastmoney = totalmoney-tz #本轮失败余下本金
    successmoney = totalmoney+win_money #本轮胜利余下本金
    print("现有资金投注比例：",f)
    print("投注金额为：",tz)
    print("可获赔金额：",hp)
    print("获胜净奖金：",win_money)
    print(f"本金 {totalmoney} 如果输了，剩余本金：{lastmoney}")
    print(f"本金 {totalmoney} 如果赢了，剩余本金：{successmoney}")
    return caly(totalmoney=caly(totalmoney=lastmoney))
def consts(money):
    list_l = []
    for  i in range(10):
        lm = caly()
        list_l.append(lm)
    print(list_l)



if __name__ == '__main__':
    d = read_excel(file="./除妖.xlsx",sheet_name = 'Sheet1')
    for i in d:
        print(i)
    print(d)
    print(1==True)
    print(0==False)
    print(time.ctime())
    print(time.localtime())
    #获取本地时间
    ltime = time.localtime()
    # tm_year=2022, tm_mon=12, tm_mday=8, tm_hour=10, tm_min=1, tm_sec=21, tm_wday=3, tm_yday=342, tm_isdst=0
    ctime = time.ctime()
    #格式化
    ftime = time.strftime('%Y-%m-%d %H:%M:%S', ltime)
    print(time.strftime('%Y-%m-%d %H:%M:%S', ltime))
    #转换成时间戳
    print("通过...", ctime,time.mktime(ltime))
    if ftime > '2023-01-06 14:42:48':
        print("现在的时间大于：2023-01-06 14:42:48")
    YMD = time.strftime("%Y-%m-%d", ltime)
    gameId = '32'
    if ftime < f"{YMD} 12:00:00":
        gameId = '73'  # 73
    print("当前gameId："+gameId)
    ctime.format()
    # exwriter = pd.ExcelWriter(path='./除妖测试.xlsx')
    # exwriter.write_cells(sheet_name='Worksheet',cells='A4')
    # exwriter.save()
    # d1 =read_excel(file="./除妖测试.xlsx")
    year = 3
    countyear=20
    pecent = 0.1
    ran = 1200
    print(total_raise(y=year, c=countyear, p=0.05, lr=[1200]))
    tlist = total_raise(y=year, c=countyear, p=0.05, lr=[1200])
    print(year_count(tlist))
    ycount = year_count(tlist)
    s = 0
    for i in ycount.values():
        s+= i
    sd = 300*12*20
    print(countyear,'年总共花费房租：',s)

    # caly()
    # consts(money=100.00)
    '''
[ 23%]{'code': 0, 'msg': '', 'data': {'gameId': 73, 'loginType': 'h5', 'nickName': 'FZYvglAK79R7', 'sign': '6346A65E19BF66A240E6478323EB7D72', 'realNameSwitchs': 1, 'token': 'eyJhbGciOiJIUzUxMiJ9.eyJnYW1lSWQiOjczLCJhY2NvdW50SWQiOiIxMWVkNzllOGM1NDBkZjUyNTI1NDAwOWMyZjA5ODY0OCIsImV4cGlyZVRpbWUiOjE2NzE0MzI0MTYsImdyYW50VHlwZSI6ImF1dGhvcml6YXRpb24ifQ.3N8TJMgZ8bgWATDgp4t1aVSsVUFMJG1UtWjz6DKKH44YX395W-Wl7mI6oxRMcVbs8iRuGLTeqsWUPRDanoXZ1g', 'realNameResult': 1, 'indulgeSwitchs': 1, 'age': -1, 'indulgeCd': -1, 'isRegister': False, 'account': 'FZYvglAK79R7', 'refreshToken': 'eyJhbGciOiJIUzUxMiJ9.eyJnYW1lSWQiOjczLCJhY2NvdW50SWQiOiIxMWVkNzllOGM1NDBkZjUyNTI1NDAwOWMyZjA5ODY0OCIsImV4cGlyZVRpbWUiOjE2NzM0MTk2MTYsImdyYW50VHlwZSI6InJlZnJlc2hUb2tlbiJ9.n2e_ri7OTGhfFkp_7D14o-iu4Knr_Gk4SHGbEpDzwmZ3s2I61U3g9dFeqYG2s4SE4YD6oLRA5BCKVQFqEmit9Q', 'playerId': '11ed79e8c540df525254009c2f098648', 'timestamp': 1670827616}}
{'code': 0, 'msg': '', 'data': {'gameId': 73, 'loginType': 'h5', 'nickName': 'FZYvglAK79R7', 
'sign': '6346A65E19BF66A240E6478323EB7D72', 'realNameSwitchs': 1, 'token': 'eyJhbGciOiJIUzUxMiJ9.eyJnYW1lSWQiOjczLCJhY2NvdW50SWQiOiIxMWVkNzllOGM1NDBkZjUyNTI1NDAwOWMyZjA5ODY0OCIsImV4cGlyZVRpbWUiOjE2NzE0MzI0MTYsImdyYW50VHlwZSI6ImF1dGhvcml6YXRpb24ifQ.3N8TJMgZ8bgWATDgp4t1aVSsVUFMJG1UtWjz6DKKH44YX395W-Wl7mI6oxRMcVbs8iRuGLTeqsWUPRDanoXZ1g', 'realNameResult': 1, 'password': '883843', 'indulgeSwitchs': 1, 'age': -1, 'indulgeCd': -1, 'isRegister': True, 'account': 'FZYvglAK79R7', 'refreshToken': 'eyJhbGciOiJIUzUxMiJ9.eyJnYW1lSWQiOjczLCJhY2NvdW50SWQiOiIxMWVkNzllOGM1NDBkZjUyNTI1NDAwOWMyZjA5ODY0OCIsImV4cGlyZVRpbWUiOjE2NzM0MTk2MTYsImdyYW50VHlwZSI6InJlZnJlc2hUb2tlbiJ9.n2e_ri7OTGhfFkp_7D14o-iu4Knr_Gk4SHGbEpDzwmZ3s2I61U3g9dFeqYG2s4SE4YD6oLRA5BCKVQFqEmit9Q', 'playerId': '11ed79e8c540df525254009c2f098648', 'timestamp': 1670827616}, 'tour': [{'api': '/sdkCreate/touristCreate', 'gameId': '73'}]}

    '''

