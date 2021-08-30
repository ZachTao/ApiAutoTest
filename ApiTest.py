# -*-coding:utf-8 -*-
import unittest
import requests
from ReadWriteExcel import ReadWriteExcel
import HTMLTestRunner
import time


class ApiTest(unittest.TestCase):

    def test_a(self):
        filpath = r'/home/zach/pystore/PycharmProjects/ApiAutoTest/templates/ApiData.xls'
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
            if req_typ == 'get':
                r = requests.get(url_var, params=paras)
                print(r.text)
            elif req_typ == 'post':
                r = requests.post(url_var, params=paras)
                print(r.text)
            else:
                print('error,请检查测试模板文件数据')
                
    # def testA(self):
    #     fpath = (r'/home/zach/pystore/PycharmProjects/ApiAutoTest/templates/ApiData.xls')
    #     ta = ApiRequest()
    #     ta.getpms_req(fpath)


if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTests('test_a')
    runner = unittest.TextTestRunner()
    now = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())
    fp = open(now + 'result.html', 'wb')

    # 定义报告格式
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='规范性检查测试报告',
        description=u'用例执行情况:')

    # 运行测试用例
    runner.run(suite)
    # 关闭报告文件
    fp.close()
