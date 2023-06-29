import json
import unittest

import pytest
import unittestreport
import openpyxl
import allure
import requests
import yaml
import time
def func1(e:list):
    print('返回')
    return e
# @pytest.fixture()
# def test_01_login():
#     print('测试pytest')
#     assert 1==2
def robot_send(card_data):
    header={"Content-Type":"application/json","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}
    req = requests.post(url="https://open.feishu.cn/open-apis/bot/v2/hook/ca4d17e9-18dc-4ac7-b129-49dd8e83753f",
                        json=card_data, headers=header)
    print(req.json())
    pass
if __name__ == '__main__':
    print('测试第一个Python程序')
    print(func1([1, 2]))
    # up = unittestreport()
    # su = unittest.defaultTestLoader.discover('./test')
    # run = unittestreport.TestRunner(suite=su)
    # run.run()
    now_time=time.ctime()
    #time.strftime()
    print(time.ctime())
    print(now_time)
    #字符串解析成时间，提取年月日组合成想要的时间格式
    ptime=time.strptime(now_time)
    print(ptime)
    #使用localtime，直接用strftime
    lt=time.localtime()
    print(lt)
    ltime_format=time.strftime("%Y.%m.%d %H:%M:%S", lt)
    print(ltime_format)
    print(ptime.tm_year,".",ptime.tm_mon,"月",ptime.tm_mday,"日",ptime.tm_hour,ptime.tm_min,ptime.tm_sec)
    ymd=[ptime.tm_year,ptime.tm_mon,ptime.tm_mday]
    HMS=[ptime.tm_hour,ptime.tm_min,ptime.tm_sec]
    print(ymd,HMS)
    #发送请求，机器人群组消息
    card_data={
    "msg_type": "interactive",
    "card": {
        "config": {
            "wide_screen_mode": True
        },
        "elements": [
            {
                "tag": "div",
                "text": {
                    "content": "😁***SDK接口执行成功！执行时间：***",
                    "tag": "lark_md"
                }
            },
            {
                "tag": "div",
                "text": {
                    "content": "***测试报告已生成！点击前往查看！***🌞",
                    "tag": "lark_md"
                }
            },
            {
                "actions": [
                    {
                        "tag": "button",
                        "text": {
                            "content": "查看",
                            "tag": "plain_text"
                        },
                        "type": "primary",
                        "value": {
                            "key": "value"
                        },
                        "multi_url": {
                            "url": "http://10.10.51.73:62017/index.html",
                            "pc_url": "",
                            "android_url": "",
                            "ios_url": ""
                        }
                    }
                ],
                "tag": "action"
            },
            {
                "tag": "hr"
            },
            {
                "elements": [
                    {
                        "content": "来自Jenkins构建生成",
                        "tag": "lark_md"
                    }
                ],
                "tag": "note"
            }
        ],
        "header": {
            "template": "wathet",
            "title": {
                "content": f"【SDK接口报告】{ltime_format}",
                "tag": "plain_text"
                }
            }
        }
    }
    card_data=json.dumps(card_data)
    print(card_data)
    print("下面发送机器人消息")
    robot_send(card_data)
    print("发送成功")
    # with open('a.yml', 'r', encoding='utf-8') as f:
    #    ab = yaml.full_load(f)
    #    print(ab)