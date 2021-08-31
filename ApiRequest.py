# -*-coding:utf-8 -*-
import requests
from ReadWriteExcel import ReadWriteExcel
import logging
# Api请求发起,核心部分
# 需要做的是获取excel的参数，构造请求；当前暂时添加核心参数，后续补充其他功能
# 判断req_type 写if
# 获取url&params
# 写完之后怎么根unittest结合
# 结合报告、邮件、log等其他


class ApiRequest:

    def getpms_req(self, filpath):
        headers = {
            'user - agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                            '(KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.84'
        }
        get_pm = ReadWriteExcel()   # 一定要先实例化再引用类方法
        pms = get_pm.read_excel(filpath)
        for pm in pms:
            req_typ = pm['req_type']
            url_var = pm['url_val']
            # 组合params
            paras = {
                'key': pm['key'],
                'dtype': pm['rtunfmat'],
            }
            lins = pm['param'].split('&')
            linvs = str(pm['param_val']).split('&')
            for i in range(len(lins)):
                paras[lins[i]] = linvs[i]
            # print(paras)
            # 构建请求
            try:
                if req_typ == ("post" or "POST"):
                    results = requests.post(url_var, params=paras, headers=headers)
                elif req_typ == ("get" or "GET"):
                    results = requests.get(url_var, params=paras, headers=headers)
                elif req_typ == "put":
                    results = requests.put(url_var, params=paras, headers=headers)
                elif req_typ == "delete":
                    results = requests.delete(url_var, headers=headers)
                elif req_typ == "patch":
                    results == requests.patch(url_var, params=paras, headers=headers)
                elif req_typ == "options":
                    results == requests.options(url_var, headers=headers)
                response = results.json()
                print(response)
                code = response.get("reason")
                return code
            except Exception as e:
                logging.error("service is error", e)


if __name__ == '__main__':
    requ = ApiRequest()
    requ.getpms_req(r'/home/zach/pystore/PycharmProjects/ApiAutoTest/case_excel/ApiData.xls')

