import random
import os

import yaml

path = os.path.join(os.path.abspath(__file__))
print(path)
#当前绝对路径
print(os.path.abspath("setbug.py"))
initpath=os.path.join(os.path.dirname(os.path.abspath(__file__)),"__init__.py")
#当前文件所在路径，的文件夹路径
print(os.path.dirname(os.path.abspath(__file__)))
print(initpath)
# tourdata = yaml.full_load(open(r'E:\A_PythonProject\TestProject\test221010\test\yml\touristcreate.yml', 'r', encoding='utf-8'))
# print(tourdata)

{'code': 0, 'msg': '', 'data': {'gameId': 73, 'loginType': 'h5', 'nickName': 'FZp4rZy7A99e', 'sign': 'B32083F32009587B51A569C5E6F1AB49', 'realNameSwitchs': 1, 'token': 'eyJhbGciOiJIUzUxMiJ9.eyJnYW1lSWQiOjczLCJhY2NvdW50SWQiOiIxMWVkNjk4MzhhZTI2YjJlNTI1NDAwOWMyZjA5YmU1YSIsImV4cGlyZVRpbWUiOjE2Njk2Mjk3MjEsImdyYW50VHlwZSI6ImF1dGhvcml6YXRpb24ifQ.aEhV6HEs5_bFJ9DWmYNADktLEkw-PHZo_P8L-L7XgZ5-lXtcmAUSte6hggtJQJ0UGjRGfhbTUW7hJooYsvc61A', 'realNameResult': 1, 'password': '337624', 'indulgeSwitchs': 1, 'age': -1, 'indulgeCd': -1, 'isRegister': True,
                                'account': 'FZp4rZy7A99e', 'refreshToken': 'eyJhbGciOiJIUzUxMiJ9.eyJnYW1lSWQiOjczLCJhY2NvdW50SWQiOiIxMWVkNjk4MzhhZTI2YjJlNTI1NDAwOWMyZjA5YmU1YSIsImV4cGlyZVRpbWUiOjE2NzE2MTY5MjEsImdyYW50VHlwZSI6InJlZnJlc2hUb2tlbiJ9.Xs7BrRbiN2JmPQqnsjAdh6FGC5m9gJGBvbaM-JjFceq0ydANljUqzVhSsZJ3ryIfU7XPzdBG7l_w4UMGpgJvKA', 'playerId': '11ed69838ae26b2e5254009c2f09be5a', 'timestamp': 1669024921},
 'tour': [{'api': '/sdkCreate/touristCreate', 'gameId': '73'}]}