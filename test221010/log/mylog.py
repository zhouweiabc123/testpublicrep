import logging
class MyLogger(logging.Logger):
    #logging.DEBUG
    def __init__(self,logname='log1',loglevel='INFO',filename=None,):
        print('文件名:',filename)
        # 调用父类构造方法,生成日志搜集器
        super().__init__(name=logname,level=loglevel)
        #设置日志格式模板
        formater = logging.Formatter(fmt='%(asctime)s,日志器 %(name)s,等级 %(levelname)s,模块 %(module)s,函数 %(funcName)s 第%(lineno)d行,%(message)s')
        #添加渠道，如果filename不为null，使用文件形式，否则使用控制台
        if filename:
            handler_file = logging.FileHandler(filename,encoding='utf-8')
            handler = logging.StreamHandler()
        else:
            handler = logging.StreamHandler()
        #设置日志输出等级DEBUG INFO WARNING WARN ERROR exception critical
        handler.setLevel('INFO')
        #设置输出格式
        handler.setFormatter(fmt=formater)
        handler_file.setFormatter(fmt=formater)
        #渠道添加到日志搜集器上
        self.addHandler(handler)
        self.addHandler(handler_file)
        #self.info()
mylog = MyLogger(logname='logname',loglevel='INFO',filename='./test.log')
def log_test():
    mylog.info('日志封装好了调用成功第1次')
if __name__ == '__main__':
    #log = MyLogger()
    #mylog.info('日志封装好了调用成功')
    log_test()
    print("你好啊")