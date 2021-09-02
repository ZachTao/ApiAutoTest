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
    # 获取指定路径配置文件所有section的内容
    def getiniconfig(self, filename=""):
        curpath = os.path.dirname(os.path.realpath(__file__))  # 获取文件目录
        cfgpath = os.path.join(curpath, filename)
        con = configparser.ConfigParser()
        con.read(cfgpath)
        print(con.sections())
        sections = con.sections()
        for section in sections:
            print('配置文件'+section, con.options(section))
            print('配置文件'+section+'键值对', con.items(section))

    def get_email_ini(self):
        emicans = []
        curpath = os.path.dirname(os.path.realpath(__file__))  # 获取文件目录
        cfgpath = os.path.join(curpath, 'ini/myconfig.ini')
        con = configparser.ConfigParser()
        con.read(cfgpath)
        options = con.options('Email')
        for option in options:
            if option == 'receiver':
                receivers = con.get("Email", "receiver")
                receiver = receivers.split(',')
                emicans.append(receiver)
            elif option == 'cc':
                ccs = con.get("Email", "cc")
                relcc = ccs.split(',')
                emicans.append(relcc)
            elif option == 'reportdc':
                rdc = con.get("Email", "reportdc")
                lists = os.listdir(rdc)  # 列出目录的下所有文件和文件夹保存到lists
                lists.sort(key=lambda fn: os.path.getmtime(rdc + "//" + fn))  # 按时间排序
                file_new = os.path.join(rdc, lists[-1])  # 获取最新的文件保存到file_new
                emicans.append(file_new)
            else:
                golopt = con.get("Email", option)
                emicans.append(golopt)
        return emicans


if __name__ == '__main__':
    conn = GetIni()
    # conn.getiniconfig('ini/myconfig.ini')
    conn.get_email_ini()

