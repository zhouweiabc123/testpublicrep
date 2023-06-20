import time
import pandas as pd
import os
import json
import requests
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

null = None

class AutoExcel:
    def __int__(self):
        print("开始调试")

    #pandas读取Excel填写的接口信息
    def read_excel(self,file, **kwargs):
        data_dict = []
        try:
            data = pd.read_excel(file, **kwargs)
            data_dict = data.to_dict('records')
        except Exception as e:
            print(e)
        finally:
            return data_dict

    def processData(self,exceldata):
        '''
        pandas读取的一些参数数据是字符串，这里转成dict，方便转json
        :param exceldata: 读取到的excel接口数据
        :return:
        '''
        print("exceldata的类型")
        print(type(exceldata))

        #string处理成dict
        try:
            for i in range(len(exceldata)):
                exceldata[i]["请求参数"] = eval(exceldata[i]["请求参数"])
                exceldata[i]["请求头"] = eval(exceldata[i]["请求头"])
                exceldata[i]["预期响应"] = eval(exceldata[i]["预期响应"])
        except Exception as e:
            print("原始数据处理出现错误了")
            print(f"第{i}个数据有问题")
            print(exceldata[i])
            print(exceldata[99])
            print(e)

        print(exceldata[0])
        return exceldata

    #发送requests请求
    def req(self,po,url,data,head,expectresponse):
        vars = None
        '''
              po代表方法
              url是请求地址
              data代表请求参数
              head是请求头
              dcnum是当前执行的第几个接口，默认第一个
              expectresponse 是传入的预期响应，每一条用例一个预期响应
              返回一个list：发送请求的响应，已经处理成字典类；加接口请求的实际结果
        '''

        print("正在输出传入的参数..........................................")
        print(po)
        print(type(po))
        print(url)
        print(type(url))
        print(head)
        print(type(head))
        print(data)
        print(type(data))
        # 使用Excel表格数据发送请求,POST,GET,UPDATE,DELETE,判断请求方式，根据请求方式发送请求
        try:
            if po == "POST":
                res = requests.post(url=url, json=data, headers=head)
                print(res.text)
                # 响应转json
                reponse = res.json()
                print(reponse)
                # json转字典 先用json.dumps转str，再用eval()转字典，str转json用json.loads
                reponse = json.dumps(reponse)
                print(reponse)
                print(type(reponse))
                # 处理msg的值 null，强转成""，用赋值，也可用str的replace替换
                reponse = eval(reponse)
                print(reponse)
                # 获取当前用例的预期响应
                print(expectresponse)
                actualyResult = "成功"
                if reponse == expectresponse or reponse["code"] == 1:
                    print("预期响应与实际响应相同，用例通过")
                    print(actualyResult)
                    # 用例通过或失败都需回填实际响应和实际结果
                    # self.columnsWrite(actulyresponse=reponse, actualyResult=actualyResult)
                else:
                    print("预期响应与实际响应不相同，用例失败")
                    actualyResult = "失败"
                    print(actualyResult)
            elif po == "GET":
                # 这里的参数，根据data类型转换，目前传过来的data是dict类
                res = requests.get(url=url, params=data, headers=head)
                print(res)
                # 响应转json
                reponse = res.json()
                print(reponse)
                # json转字典 先用json.dumps转str，再用eval()转字典（dict），str转json用json.loads
                reponse = json.dumps(reponse)
                print(reponse)
                print(type(reponse))
                # 处理msg的值 null，强转成""，用赋值，也可用str的replace替换
                reponse = eval(reponse)
                # 获取当前用例的预期响应
                print(expectresponse)
                actualyResult = "成功"
                if reponse == expectresponse or reponse["code"] == 1:
                    print("预期响应与实际响应相同，用例通过")
                    print(actualyResult)
                    # 用例通过或失败都需回填实际响应和实际结果
                    # self.columnsWrite(actulyresponse=reponse, actualyResult=actualyResult)
                else:
                    print("预期响应与实际响应不相同，用例失败")
                    actualyResult = "失败"
                    print(actualyResult)
        except Exception as e:
            print("请求发送失败，出了错误")
            print(e)

        #返回响应数据，reponse已转成字典,以及响应结果
        result_data={}
        result_data["response"]=reponse
        result_data["actualyResult"]=actualyResult
        return result_data
    #提取响应数据，输出到Excel
    def write_tofile(self,fpathname=None,exceldata=[],resultdata=[]):
        '''
        :param fpathname:最终要写入的Excel文件名称路径，如果不传就不写
        :param exceldata:处理过后的表格用例数据
        :param resultdata:执行接口请求后的返回结果
        :return:
        '''
        print("开始调用封装后的方法")
        if fpathname:
            indexlist = []
            try:
                for dataindex in range(0, len(exceldata)):
                    print(f"第{dataindex + 1}条用例详细")
                    print(exceldata[dataindex])
                    # 改变原来exceledata的实际响应和实际结果，为了接下来接口执行后的用例信息写入
                    exceldata[dataindex]["实际响应"] = resultdata[dataindex]["response"]
                    exceldata[dataindex]["实际结果"] = resultdata[dataindex]["actualyResult"]
                    # 把exceldata里字典数据类型转成json类型，方便使用DataFrame
                    exceldata[dataindex]["请求参数"] = json.dumps(exceldata[dataindex]["请求参数"])
                    exceldata[dataindex]["请求头"] = json.dumps(exceldata[dataindex]["请求头"])
                    exceldata[dataindex]["预期响应"] = json.dumps(exceldata[dataindex]["预期响应"])
                    exceldata[dataindex]["实际响应"] = json.dumps(exceldata[dataindex]["实际响应"])
                    # 索引标记
                    indexlist.append(dataindex)
                    # 生成DataFrame
                print(exceldata)
                excel_df = pd.DataFrame(exceldata, index=indexlist)
                print("下面是生成的DataFrame表")
                print(excel_df)
                # excel_df.to_excel(fpathname,index=False)
            except Exception as e:
                print("出现错误了，下面是错误信息")
                print(e)

        else:
            pass
        return None
if __name__ == '__main__':
    '''
    ID = "id"
    XPATH = "xpath"
    LINK_TEXT = "link text"
    PARTIAL_LINK_TEXT = "partial link text"
    NAME = "name"
    TAG_NAME = "tag name"
    CLASS_NAME = "class name"
    CSS_SELECTOR = "css selector"
    '''
    print(time.ctime())
    time_start = time.perf_counter()
    #WEB网页UI自动化
    wb = webdriver.Chrome()
    #隐示等待，默认最长等待时间，如果超过了就退出
    wb.implicitly_wait(10)
    wb.maximize_window()
    wb.get("https://www.baidu.com")
    e1 = wb.find_element("id", "kw").send_keys("123")
    #显示等待，指定时间内等待某个元素出现后，继续执行下面的操作，否则退出
    e2 = WebDriverWait(wb, 3, 0.5).until(lambda x: x.find_element("xpath", '//*[@id="su"]'))
    # element = WebDriverWait(driver, 10).until(lambda x: x.find_element(By.ID, "someId")) \n
    print(e2)
    e2.click()
    #强制等待，无论怎么样，都强制等待指定的时间后再执行
    sleep(3)
    wb.quit()

    print("调试Excel接口测试")
    ae=AutoExcel()
    exceldt=ae.read_excel(file="./按行写入.xlsx")
    pro_exceldt=ae.processData(exceldt)
    print(pro_exceldt[3])
    onedata=pro_exceldt[4]
    twodata=pro_exceldt[3]
    data_list=[onedata,twodata]
    print("开始请求接口")
    #现在不拿出错误的第几百条规矩来展示 ，以后会有更多被封在雪下，又深藏再心中
    #单个接口用例请求测试
    reqdata1=ae.req(po=twodata["请求方式"],data=twodata["请求参数"],url=twodata["URL"],head=twodata["请求头"],expectresponse=twodata["预期结果"])
    reqdata=ae.req(po=onedata["请求方式"],data=onedata["请求参数"],url=onedata["URL"],head=onedata["请求头"],expectresponse=onedata["预期结果"])
    print("请求成功")
    print(reqdata)
    reqdatas=[reqdata1,reqdata]
    print("多接口用例信息")
    print(reqdatas)
    print(data_list)
    print("===="*20)
    #现在填入执行用例的结果和响应
    pro_exceldt[4]["实际结果"]=reqdata["actualyResult"]
    pro_exceldt[4]["实际响应"]=reqdata["response"]
    print("下面输出这条变更过数据的用例信息")
    print(pro_exceldt[4])
    #这里需要把这条数据里面的dict转换成str，才好生成DataFrame数据写入Excel文件里
    demoyl_toexcel=pro_exceldt[4]
    demoyl_toexcel["请求参数"]=json.dumps(demoyl_toexcel["请求参数"])
    demoyl_toexcel["请求头"]=json.dumps(demoyl_toexcel["请求头"])
    demoyl_toexcel["预期响应"]=json.dumps(demoyl_toexcel["预期响应"])
    demoyl_toexcel["实际响应"]=json.dumps(demoyl_toexcel["实际响应"])
    demoyl_df=pd.DataFrame(demoyl_toexcel,index=[1])
    print(demoyl_df)
    print(type(demoyl_toexcel["请求参数"]))
    #demoyl_df.to_excel("./demoyl.xlsx",index=False)
    print("写入Excel成功")
    #多个接口用例请求测试
    ae.write_tofile(fpathname="xxx",exceldata=data_list,resultdata=reqdatas)
    for i in data_list:
        pass
    #计算运行时间
    print(time.ctime())
    print(type(time.ctime()))
    time_end = time.perf_counter()
    run_time = time_end - time_start
    print("运行时长：", run_time)
    if run_time-10 < 1:
        print("差点超过10秒")
    #运行时长run_time

