from study_pandas import read_excel
#excel_data = read_excel(file="./shuju.xlsx",sheetname="")
import urllib.parse
import re
import requests
import base64
def urlGet(html):
    '''
    抓取图片
    '''
    header = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}
   #发送get请求到网页
    res = requests.get(url=html,headers=header)
    #整个返回
    url_text = res.text
    print(url_text)
    #正则查找链接"img max-width='600' src='https://p9.itc.cn/q_70/images01/20220209/fdd9060b2c7d4e058bd97f3ba65d0310.jpeg'"
    #ObjURL: "https://inews.gtimg.com/newsapp_bt/0/13550277465/1000"
    part_re = 'data-src="(.*?)"'
    img_urls= re.findall(part_re,url_text,re.S)
    for i in img_urls:
        i = str.encode(i)
        print(base64.b64decode(i))
    print(img_urls)
if __name__ == '__main__':
    word = "加藤惠"
    word = urllib.parse.quote(word)
    urlGet("http://news.sohu.com/a/521665655_121194359")
    print(word)



