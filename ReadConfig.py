# -*-coding:utf-8 -*-
'''
用ConfigParser模块中的ConfigParser类读取ini文件，然后使用ConfigParser类中的get方法，然后读取到value值
'''
import os
import configparser

curpath = os.path.dirname(os.path.realpath(__file__))  # 获取文件目录
cfgpath = os.path.join(curpath, "myconfig.ini")  # 读取到本机的配置文件
# 调用读取配置模块中的类
conf = configparser.ConfigParser()
conf.read(cfgpath)

sections = conf.sections()
print('获取配置文件所有的section', sections)
options = conf.options('HTTP')
print('获取指定section下所有option', options)
items = conf.items('HTTP')
print('获取指定section下所有的键值对', items)

# 调用get方法，然后获取配置的数据（获取指定的section下的option的值）
host = conf.get("database", "host")
name = conf.get("database", "username")
psw = conf.get("database", "password")
port = conf.get("database", "port")
database = conf.get("database", "databasename")
print(host, name, psw, port, database)

