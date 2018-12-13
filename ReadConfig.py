#coding=utf-8

import os
import configparser
proDir=os.path.split(os.path.realpath(__file__))[0]
confPath=os.path.join(proDir,'conf.ini') #获取conf.ini路径
conf=configparser.ConfigParser()
conf.read(confPath)
class ReadConfig:
    def __init__(self):
        pass

    @staticmethod
    def get_URL(name):
        url = conf.get("URL", name)
        return url

    @staticmethod
    def get_Email(name):
        value = conf.get("EMAIL", name)
        return value

    @staticmethod
    def get_Driver(name):
        value = conf.get("DRIVER", name)
        return value

