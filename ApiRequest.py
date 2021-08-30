# -*-coding:utf-8 -*-
import requests
from ReadWriteExcel import ReadWriteExcel
# Api请求发起,核心部分
# 需要做的是获取excel的参数，构造请求；当前暂时添加核心参数，后续补充其他功能
# 判断req_type 写if
# 获取url&params
# 写完之后怎么根unittest结合
# 结合报告、邮件等其他


class ApiRequest:

    def get_params(self,filpath):
        get_pm = ReadWriteExcel()   # 一定要先实例化再引用类方法
        pms = get_pm.read_excel(filpath)
        for pm in pms:
            req_typ = pm['req_type']
            url_var = pm['url_val']
            # 组合params
            paras={
                'key': pm['key'],
                'dtype': pm['rtunfmat'],
            }
            lins = pm['param'].split('&')
            linvs = str(pm['param_val']).split('&')
            for i in range(len(lins)):
                paras[lins[i]] = linvs[i]
            # print(paras)
            # 构建请求
            if req_typ == 'get':
                r = requests.get(url_var, params=paras)
                print(r.text)
            elif req_typ == 'post':
                r = requests.post(url_var, params=paras)
                print(r.text)


if __name__ == '__main__':
    requ = ApiRequest()
    requ.get_params(r'/home/zach/pystore/PycharmProjects/ApiAutoTest/templates/ApiData.xls')

