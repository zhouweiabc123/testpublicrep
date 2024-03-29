from study_pandas import read_excel
from sqlalchemy import create_engine
import pymysql
import pandas as pd
import time
def get_NowTime():
    #获取本地时间
    ltime = time.localtime()
    #格式化
    ftime = time.strftime('%Y-%m-%d %H:%M:%S',ltime)
    print(ftime)
    return ftime
# yq = None
def read_zk(pathExcelFiel):
    #r"C:\Users\htsd\Downloads\【平台技术】需求管理_中控需求.xlsx"
    #r"C:\Users\htsd\Downloads\【平台技术】需求管理_渠道接入.xlsx"
    yq = 0
    zkdata = read_excel(pathExcelFiel)
    for i in zkdata:
        print(i)
        # endtime = i['结束时间']
        # print(endtime)
        # endtime = str(endtime)
        # nt = get_NowTime()
        # if (endtime <= nt) and i["任务状态"] not in ["已完成","待上线","已取消"]:
        #     task = i["任务名称"]
        #     print(f"结束时间：{endtime} < 当前时间：{nt} ")
        #     print(f"任务名称：{task} 延期")
        #     yq += 1
        #print(str(endtime))
        #print(type(endtime))
    return zkdata
def work_state(data):
    '''
    任务状态  待排期 制作期 验收期 待上线 已完成 已取消 暂停中
    '''
    dpq = 0
    zzq = 0
    ysq = 0
    dsx = 0
    ywc = 0
    yqx = 0
    ztz = 0
    yq = 0
    # 延期任务list  delay task
    delaytasks = []
    for i in data:
        if i["任务状态"] == "待排期":
            dpq += 1
        elif i["任务状态"] == "制作期":
            zzq += 1
        elif i["任务状态"] == "验收期":
            ysq += 1
        elif i["任务状态"] == "待上线":
            dsx += 1
        elif i["任务状态"] == "已完成":
            ywc += 1
        elif i["任务状态"] == "已取消":
            yqx += 1
        elif i["任务状态"] == "暂停中":
            ztz += 1
        print(i)
        endtime = i['结束时间']
        print(endtime)
        endtime = str(endtime)
        nt = get_NowTime()
        if (endtime <= nt) and i["任务状态"] not in ["已完成", "待上线", "已取消"]:
            task = i["任务名称"]
            launch= i['发起人']
            development = i['开发人员']
            print(f"结束时间：{endtime} < 当前时间：{nt} ")
            print(f"任务名称：{task} 延期")
            print("任务发起人：{}".format(launch))
            print("任务开发人员：{}".format(development))
            i["是否延期"] = "是"
            delaytasks.append(i)
            yq += 1
        else:
            i["是否延期"] = "否"
    print(data)
    state_data = [{"待排期":dpq},{"制作期":zzq},{"验收期":ysq},{"待上线":dsx},{"已完成":ywc},{"已取消":yqx},{"暂停中":ztz},{"延期":yq}]
    print(state_data)
    return [state_data,data,delaytasks]

def insert_sql(dataframe,enginelink="mysql+pymysql://root:123456@localhost:3306/st?charset=utf8"):
    dataframe = pd.DataFrame(dataframe)
    '''
    dataframe:可以转成DataFrame的数据
    enginlink:数据库引擎，作为to_sql方法的con
    '''
    try:
        print("开始插入数据库")
        # 1、创建引擎，建立连接
        engine = create_engine(enginelink)
        # 2、使用pd.tosql()导入数据库
        dataframe.to_sql(name="test_df", con=engine, if_exists="append", schema="st",index=True)
        print("插入数据库成功")
    except Exception as e:
        print("出现错误了，下面是错误信息")
        print(e)
    finally:
        pass
        # 查看数据是否正常
        #pd.read_sql(sql="select * from test_df", con=engine)

if __name__ == '__main__':
    #任务状态  待排期 制作期 验收期 待上线 已完成 已取消 暂停中
    print("输出查看中控需求进度表")
    print("============================================" * 10)
    zk = read_zk(r"C:\Users\htsd\Downloads\【平台技术】需求管理_中控需求.xlsx")
    #zk['是否延期'] = "否"
    print("统计中控需求有效任务状态")
    ws = work_state(zk)
    print(ws)
    #调用work_state() 方法，用处理后的data生成DataFrame对象
    df = pd.DataFrame(ws[1])
    zk_delaydf = pd.DataFrame(ws[2])
    #获取指定数据的是在第几行
    print("找到任务名称为  例维公告模板优化的index，通过index确定行号")
    column_num = df[df['任务名称'] == '例维公告模板优化'].index
    print(column_num)
    column_num = df[df['任务名称'] == '例维公告模板优化'].index.to_numpy() #numpy数组
    print(column_num)
    column_num = df[df['任务名称'] == '例维公告模板优化'].index[0] #只有一个并且想要整数，用子集
    print("index值需加2")
    print(column_num)
    print(column_num+2)
    df.to_excel("./zkdata.xlsx")
    #生成中控延期需求表，写入
    zk_delaydf.to_excel("./ZKdelaytask.xlsx")
    print("写入成功")
    print("============================================" * 10)
    print("输出查看渠道接入需求")
    print("============================================"*10)
    qd = read_zk(r"C:\Users\htsd\Downloads\【平台技术】需求管理_渠道接入.xlsx")
    #print("统计中控需求有效任务状态")
    ws = work_state(qd)
    # print(ws)
    print("统计渠道接入需求有效任务状态")
    qdws =work_state(qd)
    print(qdws)
    #生成渠道接入延期需求表，写入
    qd_delaydf = pd.DataFrame(ws[2])
    qd_delaydf.to_excel("./QDdelaytask.xlsx")
    print("写入成功")
    #总共需求
    totalcount = 0
    for total in ws[0]:
        n_total = total.values()
        for m in n_total:
            print(m)
            totalcount+=m

    delaycount = ws[0][-1]["延期"]
    donecount = ws[0][-4]["已完成"]
    print(f"已完成需求：{donecount}")
    print(f"延期需求：{delaycount}")
    #没有延期状态需求，是根据时间判定的，所以需求总数需要再减去延期需求数 delaycount
    print(totalcount-delaycount)
    # 插入数据库
    #insert_sql(ws[1])
    # #查看数据是否正常
    enginelink = "mysql+pymysql://root:123456@localhost:3306/st?charset=utf8"
    # con = pymysql.connect(user="root",password="123456",port=3306,host="localhost",database="st",charset="utf8" )
    con = create_engine(enginelink)
    sql_read = pd.read_sql(sql="test_df", con=con.connect())  # sql可以是表名，也可以是sql语句
    print(sql_read)
    # sql_read.drop(columns=[1])
    # sql语句查询
    # con.connect().execute("sql语句").fetchall()
    sql_read.to_excel("./testSql.xlsx",index=False)#False表示不插入index列
    tsql = read_zk("./testSql.xlsx")
    print(tsql)
    get_NowTime()