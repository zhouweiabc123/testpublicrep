import logging
log = logging.Logger(name='studylog')
handler_stream = logging.StreamHandler()
handler_file = logging.FileHandler(filename='./test.log',encoding='utf-8')
f="%(asctime)s,日志器 %(name)s,等级 %(levelname)s,模块 %(module)s,%(funcName)s函数第%(lineno)d行,%(message)s"
formatter = logging.Formatter(f)
handler_stream.setLevel(level="INFO")
handler_stream.setFormatter(fmt=formatter)
handler_file.setLevel(level='DEBUG')
handler_file.setFormatter(fmt=formatter)
log.addHandler(handler_stream)
log.addHandler(handler_file)

def log_info():
    log.info('测试日志')
    log.debug('debug级别日志写入日志文件')
if __name__ == '__main__':
    #log.info("第一个日志")
    log_info()
