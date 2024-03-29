import redis
import pymysql
import pandas as pd
from test221010.public.WorkReport import read_zk
nan = ""
import json
from pandas._libs.tslibs.timestamps import Timestamp
import time
from study_pandas import read_excel
def redisQuery():
    #建立redis连接
    r = redis.Redis(host='127.0.0.1',port=6379,db=0)
    #print(r.hget(name='recharge:month:10', key='11ed50e00ef950f95254009c2f09b7e5_32'))
    one =r.get("one").decode(encoding="utf8")
    #r.set()
    print(one)
    print(r.lrange("testlist",0,2))
    r.hset("testdict",key="d",value="HELLO")
    #读取Excel数据，插入redis库
    testsql = read_zk(r"E:\A_PythonProject\TestProject\test221010\public\testSql.xlsx")
    print(testsql)
    for ts in testsql:
        print(ts["开始时间"])
        print(type(ts["开始时间"]))
    # 转成字符串才能插入，不能插入list
    testsql = str(testsql)
    print(type(testsql))
    r.hset("testdict",key="testsql",value=testsql)
    print("插入ExcelData成功")
    # 查询redis插入的hash数据
    hs_query = r.hgetall("testdict")
    print(type(hs_query))
    print(r.hgetall("testdict"))
    #开始处理组装
    vs = []
    ks = []
    for v in hs_query.values():
        v=v.decode("utf8")
        print(v)
        vs.append(v)
    for k in hs_query.keys():
        k=k.decode("utf8")
        print(k)
        ks.append(k)
    # redis查出来，zip打包，组装好原数据
    test_dict = dict(zip(ks, vs))
    print(test_dict)
    #关闭连接
    r.close()
    print("下面是DataFrame数据")
    #转换redis查询出来的数据，字符串转成DataFrame
    #df_test_dict = pd.DataFrame(test_dict,index=[0])
    #df_test_dict = df_test_dict.to_dict("records")
    df_test_dict = test_dict
    print(df_test_dict)
    #print(df_test_dict.to_dict("records"))#DataFrame转成list
    print(df_test_dict["testsql"])
    dtd = df_test_dict["testsql"]
    print(type(dtd))
    dtd = eval(dtd)
    print(type(dtd))
    #redis查询转换成功，输出查看
    print("转换redis查出的数据，为转换成DataFrame做准备")
    for d in dtd:
        print(d)
    print(dtd)
    print(pd.DataFrame(dtd))
    redis_dtd = pd.DataFrame(dtd)
    redis_dtd.to_excel("./redisExcel.xlsx",index=False)
    #将‘testsql’转成原来的list

    # conn=pymysql.connect(
    #     host='111.231.57.24',
    #     port=2433,
    #     user='htdevelop66',
    #     password='grwkz8FCYejPMfIC',
    #     db='db_hhy_games',
    #     charset='utf8'
    #
    # )
def mysqlQuery():
    #连接MySQL并查询
    sql_data ={#连接参数
        'host':'localhost',
        'port':3306,
        'user':'root',
        'password':'123456',
        'db':'st',
        'charset':'utf8'
    }
    #建立连接
    conn = pymysql.connect(
        host=sql_data['host'],
        port=sql_data['port'],
        user=sql_data['user'],
        password=sql_data['password'],
        database=sql_data['db'],
        charset=sql_data['charset']
    )
    print(conn,1213)
    #创建游标
    cur=conn.cursor()
    print('游标创建完成')
    print(cur.execute('select * from test_df'))#查询语句
    #print(cur.fetchmany(2))，选取2个查看
    #转换数据库查询出来的数据，为转换DataFrame做准备
    sql_querys = []
    new_querys = []
    testsql = read_zk(r"E:\A_PythonProject\TestProject\test221010\public\testSql.xlsx")
    sql_keys = []
    #数据库查出来的不会带表头，这里需要获取
    for sk in testsql[0].keys():
        print(sk)
        sql_keys.append(sk)
    print(sql_keys)
    print("keys类别：",type(sql_keys))
    for i in cur.fetchmany(size=5):
        print(i)
        i = list(i)
        sql_querys.append(i)
        print(type(i))
        #zip打包成字典并添加list
        print(dict(zip(sql_keys, i)))
        new_querys.append(dict(zip(sql_keys, i)))
    testsql = read_zk(r"E:\A_PythonProject\TestProject\test221010\public\testSql.xlsx")
    print(testsql[0].keys())
    print(new_querys)
    # print(cur.fetchall())#选取所有
    # sql_query=cur.execute('select * from test_df;')
    # print(sql_query)
    cur.close()#关闭游标
    conn.close()#关闭连接
if __name__ == '__main__':
    #eval()
    redisQuery()
    mysqlQuery()