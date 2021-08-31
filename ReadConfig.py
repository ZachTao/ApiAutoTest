# -*-coding:utf-8 -*-
import configparser
import os
"""
封装类读取配置文件信息
# 调用get方法，然后获取配置的数据（获取指定的section下的option的值） 
sections = conf.sections()
print('获取配置文件所有的section', sections)
options = conf.options('HTTP')
print('获取指定section下所有option', options)
items = conf.items('HTTP')
print('获取指定section下所有的键值对', items)
# 已经通过items获取所有键值对，暂时不再单独获取值
host = conf.get("database", "host")
name = conf.get("database", "username")
psw = conf.get("database", "password")
port = conf.get("database", "port")
database = conf.get("database", "databasename")
print(host, name, psw, port, database)
"""


class GetIni:
    def getiniconfig(self, filename=""):
        curpath = os.path.dirname(os.path.realpath(__file__))  # 获取文件目录
        cfgpath = os.path.join(curpath, filename)
        con = configparser.ConfigParser()
        con.read(cfgpath)
        print(con.sections())
        sections = con.sections()
        items = con.items()
        for section in sections:
            print('配置文件'+section, con.options(section))
            print('配置文件'+section+'键值对', con.items(section))


if __name__ == '__main__':
    conn = GetIni()
    conn.getiniconfig('myconfig.ini')

