import urllib.parse

import requests
kw_name = urllib.parse.quote("李易峰")#转码
print(kw_name)
unquote_kw = urllib.parse.unquote(kw_name)#解码
print(unquote_kw)
head = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"}
rew = requests.get(url='https://www.baidu.com', params=kw_name)
rew.encoding='usf-8'
#assert rew.status_code == 1
print(rew.text)
url_get = "http://10.10.10.30:8083/ver/get"
data = {
    "native": 1,
    "mini": 1,
    "web": 1456,
    "ver": 2322
}
url_json1 = "http://10.10.10.30/tjj_client/resource/output_5E112767.json"
r = requests.get(url=url_get,json=data)
print(r.text)
r_json1 = requests.get(url_json1)
print(r_json1.text)
def fengshen_getmethod(url,data):
    result_fsget =requests.get(url,data)
    return result_fsget.text
def fengshen_postmethod(url,json):
    result_fspost = requests.post(url,json)
    return result_fspost.text
if __name__ == '__main__':
    urls = {}
    datas = {}
