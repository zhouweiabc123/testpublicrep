import ddddocr
#安装模块 pip install ddddocr -i https://pypi.douban.com/simple
#图片识别
def identifyImg(img_name):
    #1、创建DdddOcr
    ocr=ddddocr.DdddOcr()
    #2、打开read图片
    with open(img_name,"rb") as f:
        img_bytes=f.read()
        print(img_bytes)
    #print(img_bytes)
    #3、调用识别方法识别
    result_checknum=ocr.classification(img_bytes)
    print("识别结果,截图的图片验证码为：",result_checknum)
    return result_checknum
if __name__ == '__main__':
    identifyImg("check.png")