#coding=utf-8
import threading
import logging,os
from datetime import datetime
proDir=os.path.split(os.path.relpath(__file__))[0]

class Log:

    def __init__(self):
       self.proDir = os.path.split(os.path.relpath(__file__))[0]
        #创建日志文件路径
       self.logfilepath=os.path.join(self.proDir,'log')
       if not os.path.exists(self.logfilepath):
           os.mkdir(self.logfilepath)
       self.logpath=os.path.join(self.logfilepath,datetime.now().strftime("%Y%m%d%H%M%S"))
       if not os.path.exists(self.logpath):
           os.mkdir(self.logpath)

       log_file=os.path.join(self.logpath,'result.log')

       #设置输出格式
       log_farmat = '[%(asctime)s][%(levelname)s][%(filename)s]:%(lineno)d %(message)s'
       #logging.basicConfig(format=log_farmat,filename=log_file,level=logging.DEBUG)

       #日志输出到屏幕
       consle=logging.StreamHandler()
       consle.setLevel(logging.DEBUG)
       #日志输出到文件
       file = logging.FileHandler(log_file,mode='w',encoding='UTF-8')
       file.setLevel(logging.INFO)
       #设置输出到屏幕的格式
       fomater=logging.Formatter(log_farmat)
       consle.setFormatter(fomater)
       file.setFormatter(fomater)

       self.logger=logging.getLogger()
       self.logger.setLevel(logging.DEBUG)
       self.logger.addHandler(consle)
       self.logger.addHandler(file)


    def get_logger(self):
        """
                get logger
                :return:
        """
        return self.logger

    def get_report_path(self):
        reportpath = os.path.join(self.logpath, 'report.html')
        return reportpath

    def get_result_path(self):

        return self.logpath

class MyLog:
    log=None
    mutex=threading.RLock()

    def __init__(self):
        pass

    @staticmethod
    def get_log():
        if MyLog.log is None:
            MyLog.mutex.acquire()
            try:
                MyLog.log=Log()
            finally:
                MyLog.mutex.release()
        return MyLog.log


if __name__=="__main__":
    log=MyLog.get_log()
    logger=log.get_logger()
    logger.info('nihao')
    logger.debug('oooo')