import time
import pandas as pd
import os
from study_pandas import read_excel
import json
import requests
from time import sleep
null = ""
class PandasWrite:
    def __init__(self):
        print("开启调试")
    def  pdWrite(self,file_name='按行写入.xlsx',sheet_name="Sheet1"):
        #获取当前excel文件file_name 的绝对路径
        cur_dir = os.path.join(os.path.dirname(__file__),file_name)
        print("文件当前地址："+cur_dir)
        print("表名："+sheet_name)
        return cur_dir
    def columnsWrite(self,actulyresponse=None,actualyResult="成功",excelhead=("用例编号","模块","优先级","标题","URL","前置条件","请求方式",
                                   "请求头","请求参数","预期结果","预期响应","实际响应","实际结果","环境")):
        #创建DataFrame数据类型，写入表头
        re = pd.DataFrame(columns=excelhead)
        columnsdata=[]
        expectresponse={
          "timestamp": "2023-02-06T07:18:34.381+0000",
          "status": 500,
          "error": "Internal Server Error",
          "message": "Request processing failed; nested exception is java.lang.NullPointerException",
          "path": "/login"
        }
        #此处时间戳有变化，为了用例能成功，时间戳改成一样的
        # if actulyresponse:
        #     print(1111111111111111111111111111111111)
        #     expectresponse = actulyresponse
        #print(expectresponse)
        #print(type(expectresponse))
        #添加两行数据
        re.loc[0] = ["1","登录","高","密码错误gm中控登录失败","http://10.10.10.4:8008/central/login","输入的账号密码不对","POST",
                     "{'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}",
                     "{'userName':'admin','password':'21232f297a57a5a743894a0e4a801fc3'}","失败",expectresponse,actulyresponse,actualyResult,"正式环境"]
        #设置DataFrame指定单元格值，re._set_value(index,column,value)，re.loc(index,column)=value
        #re.loc[1] = ["a","b","c"]
        print("开始写入行")
        #写入Excel文件
        re.to_excel(self.pdWrite())
        print("写入成功")
    #用例执行后，响应回填到Excel表格里
    def columnsUpdate(self):
        pass
    def rowsWrite(self):
        #按列写入
        print("开始按列写入")
        #字典里的元素，data2 为表头，list里面的第一列的第几行的元素
        re = pd.DataFrame({"data2":["一","二","三"],"data3":["one","two","three"]})
        re.to_excel(self.pdWrite(),startcol=0,index=False)
        print("按列写入成功")
    def processData(self,exceldata):
        print("exceldata的类型")
        print(type(exeldata))
        # for i in exeldata:
        #     print(type(i))
        #     print(i)
            # 字符串转字典
            # i["请求参数"] = eval(i["请求参数"])
            # i["请求头"] = eval(i["请求头"])
            # i["预期响应"] = eval(i["预期响应"])
            # print(i["请求参数"])
            # print(type(i["请求参数"]))
            # print(i["请求头"])
            # print(type(i["请求头"]))
            # print(i["请求参数"])
            # print(type(i["预期响应"]))
            # print(i["预期响应"])
            # i["预期响应"] = eval(i["预期响应"])
        #string处理成dict
        for i in range(len(exeldata)):
            exeldata[i]["请求参数"] = eval(exeldata[i]["请求参数"])
            exeldata[i]["请求头"] = eval(exeldata[i]["请求头"])
            exeldata[i]["预期响应"] = eval(exeldata[i]["预期响应"])
        print(exeldata)
        return exceldata
    def req_01(self,exeldata):
        # 使用Excel表格数据发送请求,POST,GET,UPDATE,DELETE,判断请求方式，根据请求方式发送请求
        if exeldata[0]["请求方式"] == "POST":
            res = requests.post(url=exeldata[0]["URL"], data=exeldata[0]["请求参数"], headers=exeldata[0]["请求头"])
            # 响应转json
            reponse = res.json()
            # json转字典 先用json.dumps转str，再用eval()转字典，str转json用json.loads
            reponse = json.dumps(reponse)
            #reponse = eval(reponse)
            expectresponse = exeldata[1]["预期响应"]
            print(expectresponse)
            actualyResult = "成功"
            if reponse == expectresponse:
                print("预期响应与实际响应相同，用例通过")
                # 用例通过或失败都需回填实际响应和实际结果
                #self.columnsWrite(actulyresponse=reponse, actualyResult=actualyResult)
            else:
                print("预期响应与实际响应相同，用例失败")
                actualyResult = "失败"
            return [reponse, actualyResult]
            # self.columnsWrite(actulyresponse=reponse, actualyResult=actualyResult)
            # 调用修改方法，修改Excel的实际响应和实际结果
    def req_02(self,exeldata):
        # 使用Excel表格数据发送请求,POST,GET,UPDATE,DELETE,判断请求方式，根据请求方式发送请求
        if exeldata[1]["请求方式"] == "POST":
            res = requests.post(url=exeldata[1]["URL"], data=exeldata[1]["请求参数"], headers=exeldata[1]["请求头"])
        # 响应转json
        print(res)
        print(type(res))
        reponse = res.json()
        print(reponse)
        # json转字典 先用json.dumps转str，再用eval()转字典，str转json用json.loads
        reponse = json.dumps(reponse)
        print(reponse)
        print(type(reponse))
        #reponse = eval(reponse)
        expectresponse = exeldata[1]["预期响应"]
        print(expectresponse)
        actualyResult = "成功"
        if reponse == expectresponse:
            print("预期响应与实际响应相同，用例通过")
            # 用例通过或失败都需回填实际响应和实际结果
            #self.columnsWrite(actulyresponse=reponse, actualyResult=actualyResult)
        else:
            print("预期响应与实际响应相同，用例失败")
            actualyResult = "失败"
        return [reponse,actualyResult]
            #self.columnsWrite(actulyresponse=reponse, actualyResult=actualyResult)
        # 调用修改方法，修改Excel的实际响应和实际结果
    #执行接口请求方法
    def req(self,po,url,data,head,expectresponse):
        vars = None
        '''
              po代表方法
              url是请求地址
              data代表请求参数
              head是请求头
              dcnum是当前执行的第几个接口，默认第一个
              expectresponse 是传入的预期响应，每一条用例一个预期响应
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
        if po == "POST":
            res = requests.post(url=url, data=data, headers=head)
            # 响应转json
            reponse = res.json()
            print(reponse)
            # json转字典 先用json.dumps转str，再用eval()转字典，str转json用json.loads
            reponse = json.dumps(reponse)
            print(reponse)
            print(type(reponse))
            #处理msg的值 null，强转成""，用赋值，也可用str的replace替换
            reponse = eval(reponse)
            #获取当前用例的预期响应
            #expectresponse = exeldata[1]["预期响应"]
            #dcnum = 0
            #expectresponse = data[dcnum]["预期响应"]
            print(expectresponse)
            actualyResult = "成功"
            if reponse == expectresponse or reponse["code"] == 1:
                print("预期响应与实际响应相同，用例通过")
                # 用例通过或失败都需回填实际响应和实际结果
                #self.columnsWrite(actulyresponse=reponse, actualyResult=actualyResult)
            else:
                print("预期响应与实际响应相同，用例失败")
                actualyResult = "失败"
        return [reponse, actualyResult]

if __name__ == '__main__':
    print(time.ctime())
    time_start = time.perf_counter()
    pw = PandasWrite()
    #pw.pdWrite(sheet_name="1")
    #pw.columnsWrite()
    #pw.rowsWrite()

    #查看写入的Excel数据是否正确,转化Excel的数据方便拿来用
    exeldata = read_excel("./按行写入.xlsx",sheet_name = "Sheet1")
    exeldata = pw.processData(exeldata)
    print("输出处理后的data")
    print(exeldata)
    # for i  in range(len(exeldata)):
    #     exeldata[i]["请求参数"] = eval(exeldata[i]["请求参数"])
    #     exeldata[i]["请求头"] = eval(exeldata[i]["请求头"])
    #     exeldata[i]["预期响应"] = eval(exeldata[i]["预期响应"])
    # print("exceldata的类型")
    # print(type(exeldata))
    # for i in exeldata:
    #     print(type(i))
    #     print(i)
    #     #字符串转字典
    #     i["请求参数"] = eval(i["请求参数"])
    #     i["请求头"] = eval(i["请求头"])
    #     i["预期响应"] = eval(i["预期响应"])
    #     print(i["请求参数"])
    #     print(type(i["请求参数"]))
    #     print(i["请求头"])
    #     print(type(i["请求头"]))
    #     print(i["请求参数"])
    #     print(type(i["预期响应"]))
    #     print(i["预期响应"])
    #     #i["预期响应"] = eval(i["预期响应"])
    #     print(exeldata)

    #使用Excel表格数据发送请求,POST,GET,UPDATE,DELETE,判断请求方式，根据请求方式发送请求
    # pw1 = PandasWrite()
    # req1 = pw1.req_01(exeldata=exeldata)
    #解决Max retries exceeded with url

    req1 = pw.req_01(exeldata=exeldata)
    req2 = pw.req_02(exeldata=exeldata)
    #req3 = pw.req(po=exeldata[2]['请求方式'],url=exeldata[2]['URL'],data=exeldata[2]['请求参数'],head=exeldata[2]['请求头'])
    #req2 = pw.req(po=exeldata[1]['请求方式'], url=exeldata[1]['URL'], data=exeldata[1]['请求参数'],head=exeldata[2]['请求头'])
    #批量处理实际结果和实际响应
    get_vars = {}#参数字典
    list_vars = []#多参数列表
    dict_use_var = {}#需要使用到的参数
    for td in range(0,len(exeldata)):
        #pw = PandasWrite()
        print("正在输出exeldata的每一条内容")
        print(exeldata[td])
        extd = exeldata[td]
        #拿到预期响应，用来跟实际响应做对比
        exresponse = extd["预期响应"]
        print("输出预期响应")
        print(extd["预期响应"])
        #如果接口需要使用到提取的参数
        use_var = extd['使用提取的参数']
        head_use_var = extd['请求头']
        #暂时只支持使用token，在请求头
        if use_var == 'token':
            #遍历所有保存的参数，找到使用的参数key，但是这里重复了，所以先写死
            dict_use_var[use_var] = list_vars[0]['token']  # 暂且写成token
            for l in list_vars:
                pass
            #因为token参数是在请求头里，所以需要添加到请求头里
            #head_use_var = extd['请求头']
            head_use_var[use_var] = dict_use_var[use_var]
            head_use_var['userId'] = '104' #需要使用userId  先写死后期优化
        req_result = pw.req(po=extd['请求方式'],url=extd['URL'],data=extd['请求参数'],head=head_use_var,expectresponse=exresponse)
        #req_result = pw.req(po=extd['请求方式'],url=extd['URL'],data=extd['请求参数'],head=extd['请求头'],expectresponse=exresponse)
        #req_result = pw.req(po=extd['请求方式'], url=extd['URL'], data=extd['请求参数'], head=extd['请求头'], dcnum=td)
        extd['实际结果'] = req_result[1]
        extd['实际响应'] = req_result[0]
        #提取参数
        var_name = extd['提取的参数']
        if var_name == 'token':
            # and 'token' in extd['实际响应']
            if extd['实际结果'] == '成功':
                print(extd['用例编号'])
                print("需要提取token")
                print(extd['实际响应']['data']['token'])
                var_token = extd['实际响应']['data']['token']
                print("提取的token值为：{}".format(var_token))
                extd['提取的参数'] = var_token
                #提取的参数添加到get_vars里
                get_vars[var_name] = var_token
                list_vars.append(get_vars)
        else:
            print("失败的用例不用提取token")



    #========================================================================================================
    # if exeldata[0]["请求方式"] == "POST":
    #     res = requests.post(url=exeldata[0]["URL"],data=exeldata[0]["请求参数"],headers=exeldata[0]["请求头"])
    #     print("发送请求")
    # #响应转json
    # reponse = res.json()
    # print(res.json())
    # # json转字典 先用json.dumps转str，再用eval()转字典，str转json用json.loads
    # reponse = json.dumps(reponse)
    # reponse = eval(reponse)
    # print(reponse)
    # print(type(reponse))
    # print(res.status_code)
    # #print(res.text)
    # print(res.reason)
    # #存放预期响应expectlist
    # expectlist = [exeldata[0]["预期响应"],exeldata[1]["预期响应"]]
    # expectresponse = exeldata[0]["预期响应"]
    # #存放实际响应actualylist
    # actualylist = []
    # #存放实际结果的resultlist
    # resultlist = []
    # print(expectresponse)
    # #为了使用例通过，把timestamp 修改成相同的
    # #expectresponse["timestamp"] = reponse["timestamp"]
    # actualyResult = "成功"
    # if reponse == expectresponse:
    #     print("预期响应与实际响应相同，用例通过")
    #     #写到原Excel，调用columnsWrite，用例通过或失败都需回填实际响应和实际结果
    #     #pw.columnsWrite(actulyresponse=reponse,actualyResult=actualyResult)
    # else:
    #     print("预期响应与实际响应相同，用例失败")
    #     actualyResult = "失败"
        #pw.columnsWrite(actulyresponse=reponse, actualyResult=actualyResult)
#=====================================================================================================================

    #req2[1] = "成功的男人"
    #exceldata 转换成DataFrame,去掉第一列,把DataFrame写入新的Excel
    # exeldata[0].pop('Unnamed: 0')
    # exeldata[0]["实际响应"] = {'1':'一'}
    # exeldata[0]["实际结果"] = req1[1]
    # exeldata[1].pop('Unnamed: 0')
    # exeldata[1]["实际响应"] = req2[0]
    # exeldata[1]["实际结果"] = req2[1]
    # exeldata[2].pop('Unnamed: 0')
    # exeldata[2]["实际响应"] = req3[0]
    # exeldata[2]["实际结果"] = req3[1]
    #转换成string,单条数据
    for ex in exeldata[0].keys():
        exeldata[0][ex] = str(exeldata[0][ex])
    print(exeldata)
    #转换成string，多条数据
    # for i in range(len(exeldata)):
    #     for excels in exeldata[i].keys():
    #         exeldata[i][ex] = str(exeldata[i][ex])
    #     print(exeldata)


    #创建DataFrame,获取Excel的长度，接下来遍历添加到datalist里做为DataFrame的data值
    print("exceldata的长度")
    print(len(exeldata))
    #生成DataFrame的准备数据，拿已经改变过的exeldata,复制写入新的Excel文件
    datalist = []
    indexs = []
    for i in range(len(exeldata)):
        print(exeldata[i])
        ext = exeldata[i]
        # if ext['提取的参数'] == 'token':
        #     # and 'token' in extd['实际响应']
        #     if ext['实际结果'] == '成功':
        #         print(ext['用例编号'])
        #         print("需要提取token")
        #         print(ext['实际响应']['data']['token'])
        #         var_token = ext['实际响应']['data']['token']
        #         print("提取的token值为：{}".format(var_token))
        #         ext['提取的参数'] = var_token
        # else:
        #     print("失败的用例不用提取token")

        #datalist.append(exeldata[i])
        datalist.append(ext)
        indexs.append(i)
    #df = pd.DataFrame(exeldata[0],index=[0])
    print("index值")
    print(indexs)
    df = pd.DataFrame(datalist, index=indexs)
    #获取列
    dfcolumns = df.columns
    print(df.columns)
    #删除指定某一列或几列，可以用[]
    df.drop(columns=dfcolumns[0],inplace=True)
    print(df)
    #写入
    df.to_excel('./test.xlsx')
    print("多条用例写入成功")
    print(list_vars)
    print(time.ctime())
    print(type(time.ctime()))
    time_end = time.perf_counter()
    run_time = time_end - time_start
    print("运行时长：", run_time)
    #调用修改方法，修改Excel的实际响应和实际结果，此方法只写入到原来的文件里
    #通过读取的Excel文件数据，写入新的Excel文件
    #多个接口执行思路，
    # 首先需要把Excel数据存起来，再把request执行过后的响应数据存起来，然后通过写入方法写入这两个接口的响应数据，和实际结果到Excel里