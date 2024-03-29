import redis
import pymysql
import pandas as pd
#from test221010.public.WorkReport import read_zk
nan = ""
NaT = ""
import json
from pandas._libs.tslibs.timestamps import Timestamp
import time
from study_pandas import read_excel
def get_NowTime():
    #获取本地时间
    ltime = time.localtime()
    #格式化
    #ftime = time.strftime('%Y-%m-%d %H:%M:%S',ltime)
    ftime = time.strftime('%Y%m%d日%H', ltime)
    #时间戳
    print("时间戳：",int(time.mktime(ltime)))
    #格式化的日期
    print("格式化日期",time.strftime('%Y-%m-%d %H:%M:%S',ltime))
    print(ftime)
    return ftime
#判断是否是周一、周五
def isMonOrFri(daytime=time.localtime()):
    #daytime = (2023, 3, 7, 16, 29, 30, 0, 65, 0)
    '''
    daytime：当前时间
    判断是周一、周五则插入redis中，monday、friday  key里面
    '''
    # 格式化，根据Timestamp判断周一周五，数据存到redis对应的key中
    tl = daytime
    tl_f = time.strftime('%Y-%m-%d %H:%M:%S', tl)
    new_tlf = time.strftime('%Y-%m-%dT%H', tl)
    print(tl)
    print(tl_f)
    print(new_tlf)
    #'2023-03-10T'
    dayname = pd.Timestamp(new_tlf).day_name()
    print(dayname)
    dayname_key = dayname.lower()
    print(dayname_key)
    if dayname == "Monday" or dayname == "Friday":
        print("今天是{}".format(dayname))
        print("记录{}数据中...".format(dayname))
        # 插入redis，周一的可以用 monday，用dayname_key
        # rc32.dfToRedis(dfexceldata=erd32, name="testdict", key="monday")
        print("记录成功!")
        #返回dayname_key 以供插入redis
        return dayname_key
    else:
        #如果不是周一周五，不作任何操作
        print("仅周一和周五需要处理记录进去，今天是{}".format(dayname))
    print(pd.Timestamp.today().strftime('%Y-%m-%d %H:%M:%S'))
    print(type(pd.Timestamp.today()))
    print(daytime)
    #pass
#判断是否是当月第一天、最后一天
def isMthStartOrEnd(td=Timestamp.today()):
    '''
    td格式：Timestamp('2023-03-06 17:17:12.950808')
    用来判断当天是不是当月第一天或最后一天，如果是就返回，返回作为插入redis的键
    '''
    #td = Timestamp.today()
    #td = Timestamp('2023-03-31 17:17:12.950808')
    print(f" {td} 不是{td.month}月开始第一天，bool值为False：",td.is_month_start)
    print("3月1号是3月的第一天：",pd.Timestamp("2023-03-01T00").is_month_start)
    print("3月31号是3月的最后一天：",pd.Timestamp("2023-03-31T00").is_month_end)
    if td.is_month_start == True:
        return "mStart"
    elif td.is_month_end == True:
        return "mEnd"
    print("判断失败,{} 非一月中第一天或最后一天".format(td))
class RedisControl:
    def __init__(self,readfile_path=r"D:\A_Python\GitProjects\ServerProject\testpublicrep\test221010\public\testSql.xlsx",host="127.0.0.1",port=6379,db=0,password=None):
        '''
        readfile：需要读取的Excel文件
        '''
        self.readfile = readfile_path
        #创建Redis连接对象
        self.r = redis.Redis(host=host,port=port,db=db,password=password)

    #读取要插入redis的Excel数据，然后返回
    def excelReadData(self):
        erd = read_excel(self.readfile)
        print(erd)
        print(type(erd))
        dictionary={}
        for d in erd:
            type(d)
        return erd

    def queryRedis(self,datatype="hash",rediskeyname="testdict",keyname="testsql",start=0,end=1):
        '''
        查出redis里面的rediskeyname,所有缓存数据
        查询出redis里面的hash数据并做简单处理
        datatype：redis数据类型，可以是 String,List,Set,Sorted set,Hash
        rediskeyname：Redis中的keyname，用来标识redis数据
        keyname：键值对，键名
        '''

        #Redis查询出来的默认是byte类，需要解码
        # 查询字符串类型
        print(self.r.get("one").decode(encoding="utf8"))
        # 查询list类型
        print(self.r.lrange("testlist",start,end)[0].decode(encoding="utf8"))
        #查询hash类型,获取所有
        hs_query = self.r.hgetall(name=rediskeyname)
        # hs_query = self.r.hget(name=rediskeyname,key=keyname)
        # hs_query = eval(hs_query)
        print(hs_query)
        # 开始处理组装
        vs = []
        ks = []
        for v in hs_query.values():
            v = v.decode("utf8")
            print(v)
            vs.append(v)
        for k in hs_query.keys():
            k = k.decode("utf8")
            print(k)
            ks.append(k)
        # redis查出来，zip打包，组装好原数据，字典类型
        test_dict = dict(zip(ks, vs))
        print(test_dict)
        return test_dict
    def setRedis(self):
        '''
        修改redis数据库接口，待开发
        '''
        pass
    def dfToRedis(self,dfexceldata,name="testdict",key="testsql"):
        '''
        插入redis
        dfexceldata：下载的Excel文件数据
        '''
        isMF = isMonOrFri()
        isMSE = isMthStartOrEnd()
        dfexceldata = str(dfexceldata)
        #如果是周一或周五，数据需插入周一或周五的key
        if isMF:
            print("isMF有值,需插入isMF")
            #key = isMF
            print(f"isMF为{isMF},key是：", key)
            # 既要插入key为monday或friday的，也要照常插入
            self.r.hset(name=name, key=isMF, value=dfexceldata)
            print(f"插入{isMF}成功！")
        #如果是月初或月尾，数据需要插入月初或月尾的key
        if isMSE:
            print("今天是月初或月尾：",isMSE)
            print("isMSE有值,需插入isMSE")
            self.r.hset(name=name, key=isMSE, value=dfexceldata)
            print(f"插入{isMSE}成功！")

        print(f"isMF为 {isMF}，isMSE为 {isMSE}，key是：",key)
        self.r.hset(name=name,key=key,value=dfexceldata)
        print("修改redis数据成功")
    def redisToDf(self,test_dict,keyname="testsql" ):
        '''
        将从redis查出来的数据再次处理成DataFrame数据类型
        test_dict:redis查询出来处理后的数据
        keyname:redis中hash数据里的键
        '''
        print("下面是DataFrame数据")
        # 转换redis查询出来的数据，字符串转成DataFrame
        df_test_dict = test_dict
        print(df_test_dict)
        # print(df_test_dict.to_dict("records"))#DataFrame转成list
        print(df_test_dict[keyname])
        dtd = df_test_dict[keyname]
        print(type(dtd))
        dtd = eval(dtd)
        print(type(dtd))
        # redis查询转换成功，输出查看
        print("转换redis查出的数据，为转换成DataFrame做准备")
        for d in dtd:
            print(d)
        print(dtd)
        df_dtd = pd.DataFrame(dtd)
        #redis查出的数据经处理成DataFrame可写入Excel
        #df_dtd.to_excel("./rdexcel.xlsx",index=False)
        print("写入Excel成功")
        print(df_dtd)
        return df_dtd

    def close(self):
        #关闭连接
        self.r.close()
    def queryRedisByDay(self,keynames=["20230306日10","20230307日10"]):
        '''
        keynames：取redis里面的dict key值，
        按天就取当天，如["20230306日10","20230307日10"]
        按周就取本周，如["monday","friday"]
        按月待开发中....
        打算想根据传入的keynames判断，
        如果是week，就取["monday","friday"]，待开发...
        如果是month，就取["月初","月末"]，按月的待开发...
        '''
        #查询出redis里面某一天的数据
        day_start = self.queryRedis(keyname=keynames[0])
        day_end = self.queryRedis(keyname=keynames[1])
        #将redis查询出来的数据转成DataFrame用来分析
        df_day_start = self.redisToDf(test_dict=day_start,keyname=keynames[0])
        df_day_end = self.redisToDf(test_dict=day_end,keyname=keynames[1])
        start_len = df_day_start.__len__()
        end_len = df_day_end.__len__()
        print("输出这天早上和下午的需求数")
        print(start_len,end_len)
        print("输出今天新增的需求")
        print(end_len-start_len)

if __name__ == '__main__':
     print(time.ctime())
     time_start = time.perf_counter()
     rc = RedisControl()
     erd = rc.excelReadData()
     qr = rc.queryRedis()
     rc.redisToDf(test_dict=qr)
     #插入
     #rc.dfToRedis(dfexceldata=erd)
     #  20230302日18 20230308日10
     insert_time_keyname = get_NowTime()
     rc.close()
     #下面插入3月2号需求数据到Redis里
     rc32 = RedisControl(readfile_path=r"C:\Users\htsd\Downloads\【平台技术】需求管理_渠道接入 (13).xlsx")
     insert_time_keyname = get_NowTime()
     erd32 = rc32.excelReadData()
     rc32.dfToRedis(dfexceldata=erd32,name="testdict",key=insert_time_keyname)
     #rc32.dfToRedis(dfexceldata=erd32, name="testdict", key="20230308日10")
     #查询插入redis的数据 20230308日10
     qr32 = rc32.queryRedis(rediskeyname="testdict")
     #20230302日14
     rc32.redisToDf(test_dict=qr32,keyname="testsql")
     #查询
     print("开始查询redis里面的数据")
     #print(rc32.queryRedis())
     print("查询完成")
     #查询某天新增需求
     rc32.queryRedisByDay()
     rc32.close()
     time_end = time.perf_counter()
     run_time = time_end - time_start
     print("运行时长：", run_time, "秒")

     #获取今天是星期几
     print("星期几")
     print(pd.Timestamp('2023-03-10T11:32:0').day_name())
     print(pd.Timestamp('2023-03-06T11:32:0').day)
     print("用数字表示  Monday == 0 ... Sunday == 6.")
     print(pd.Timestamp('2023-03-10T10:32:0').weekday())
     #获取周
     print("周")
     print(pd.Timestamp('2023-03-6T11:32:0').day_of_week)
     print(pd.Timestamp('2023-03-06T11:32:0').day_of_year)
     #获取月
     print("月")
     print(pd.Timestamp('2023-03-06T00').month_name())
     print(pd.Timestamp('2023-03-06T').month)
     get_NowTime()
     #格式化，根据Timestamp判断周一周五，数据存到redis对应的key中
     print("开始调用日期判断接口")
     #print(isMonOrFri())
     if isMonOrFri():
         print(1)
     #rc32.dfToRedis(dfexceldata=erd,key="xxxx")
     print(isMthStartOrEnd())



