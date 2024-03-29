import pymysql
import pandas as pd
from study_pandas import read_excel
from pandas._libs.tslibs.timestamps import Timestamp
import time
from sqlalchemy import create_engine,text

class MySQLControl:
    def __init__(self,sql_data ={
        #连接参数
        'host':'localhost',
        'port':3306,
        'user':'root',
        'password':'123456',
        'db':'st',
        'charset':'utf8'
    },enginelink = "mysql+pymysql://root:123456@localhost:3306/st?charset=utf8"):
        try:
            self.con = pymysql.connect(host=sql_data["host"], user=sql_data["user"], password=sql_data["password"],
                                       port=sql_data["port"], db=sql_data["db"], charset="utf8")
            self.con_df = create_engine(url=enginelink).connect()
        except Exception as e:
            print("建立连接出错，错误是：")
            print(e)


    #删除和修改待开发...
    def df_insertSql(self,filename="./redisExcel.xlsx",tablename="insert_test"):
        '''
        exceldata：pandas读取的Excel文件数据，一般为列表形式
        filename：想要插入的Excel文件名称地址
        tablename：表名
        '''
        try:
            print("开始插入数据库")
            #1、读取Excel数据
            exceldata = read_excel(filename)
            #2、创建DataFrame数据
            df_data = pd.DataFrame(data=exceldata)
            #3、to_sql()方法写入数据库  {'fail', 'replace', 'append'}
            df_data.to_sql(name=tablename, con=self.con_df, index=False, if_exists="replace")
            print("插入数据库成功")
        except Exception as e:
            print("出现错误了，下面是错误信息")
            print(e)
        finally:
            # 查看数据是否正常
            print("查看刚才插入的数据")
            pd.read_sql(sql=text(f"select * from {tablename}"), con=self.con_df)
        print("程序结束！")


    #删除、插入、修改待开发...
    def py_insertSql(self):
        pass
    def py_querySql(self,sql="select * from insert_test"):
        #创建游标
        cur = self.con.cursor()
        #通过游标的execute()方法执行sql语句
        exeute_data= cur.execute(sql)
        # 查看所有
        data=cur.fetchall()
        print(data)
        # print(cur.fetchmany(2))，选取2个查看
        #关闭游标
        cur.close()
        return data
    def df_sqldata(self,data):
        '''
        data：pymysql从数据库查出来的数据
        转换pymysql查出来的数据
        '''
        # 转换数据库查询出来的数据，为转换DataFrame做准备
        sql_querys = []
        new_querys = []
        testsql = read_excel(r"D:\A_Python\GitProjects\ServerProject\testpublicrep\test221010\public\testSql.xlsx")
        sql_keys = []
        # 数据库查出来的不会带表头，这里需要获取
        for sk in testsql[0].keys():
            print(sk)
            sql_keys.append(sk)
        print(sql_keys)
        print("keys类别：", type(sql_keys))
        for i in data:
            print(i)
            i = list(i)
            sql_querys.append(i)
            print(type(i))
            # zip打包成字典并添加list
            print(dict(zip(sql_keys, i)))
            new_querys.append(dict(zip(sql_keys, i)))
        testsql = read_excel(r"D:\A_Python\GitProjects\ServerProject\testpublicrep\test221010\public\testSql.xlsx")
        print(testsql[0].keys())
        print(new_querys)
        # print(cur.fetchall())#选取所有
        # sql_query=cur.execute('select * from test_df;')
        # print(sql_query)
        return new_querys
    def df_querySql(self,q= "select * from test_df where test_df.`index`<10 limit 1,5;"):
        '''
        q：可以是表名，也可以是查询sql语句
        查询MySQL数据库，返回的是DataFrame数据类型
        '''
        #q="st_user"
        #sqlalchemy.text转一下，sql语句才可执行
        pdsql = pd.read_sql_query(sql=text(q),con=self.con_df)
        #pdsql = pd.read_sql(sql=text(q), con=self.con_df)
        #pdsql.to_html("./a.html",encoding="utf8")
        print(pdsql)
        return pdsql
    def close(self):
        self.con_df.close()
        self.con.close()
if __name__ == '__main__':
    mysqlcon= MySQLControl()
    mysqlcon.df_querySql()
    mysqlcon.df_insertSql()
    py_sqldata= mysqlcon.py_querySql()
    dsd=mysqlcon.df_sqldata(py_sqldata)
    a = ""
    for i in dsd:
        a = [i]
        print(a)
    a=pd.DataFrame(a)
    #a.to_excel("./newsql.xlsx")
    mysqlcon.close()