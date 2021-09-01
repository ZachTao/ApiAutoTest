# -*-coding:utf-8 -*-
import unittest
import time
import requests
import logging
from parameterized import parameterized
from DealParam import DealParams
from HTMLTestRunner_PY3 import HTMLTestRunner
from logpri import MyLogging

flpath = r'/home/zach/pystore/PycharmProjects/ApiAutoTest/case_excel/ApiData.xls'
log = MyLogging().logger

class GoRequests(unittest.TestCase):

    def chuan_can(self):
        la = DealParams()
        cans = la.dealparams(filpath=flpath)
        return cans

    @parameterized.expand(chuan_can(flpath))
    # 上面返回的参数需要是List[[],[]]
    def test_rego(self, reqmethod, requrl, regparams):
        log.info("发送接口调用")
        try:
            if reqmethod == ("post" or "POST"):
                results = requests.post(requrl, regparams)
                log.info("返回结果：%s" % results)
            elif reqmethod == ("get" or "GET"):
                results = requests.get(requrl, regparams)
                log.info("返回结果：%s" % results)
            elif reqmethod == "put":
                results = requests.put(requrl, regparams)
                log.info("返回结果：%s" % results)
            elif reqmethod == "patch":
                results = requests.patch(requrl, regparams)
                log.info("返回结果：%s" % results)
            # elif reqmethod == "options":
            #     results = requests.options(requrl, headers=headers)
            # elif reqmethod == "delete":
            #     results = requests.delete(requrl, headers=headers)
            response = results.json()
            code = response.get("reason")
            self.assertIn(code, 'Return Successd!/ok', msg='返回reason不一致，测试不通过')
        except Exception as e:
            # logging.error("service is error", e)
            log.info(e)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(GoRequests))
    now = time.strftime('%Y-%m-%d %H_%M_%S')
    report_path = r"/home/zach/pystore/PycharmProjects/ApiAutoTest/resultC/"+now+"ApiTestReport.html"
    with open(report_path, "wb") as f:
        runner = HTMLTestRunner(stream=f, title="ApiTestReport", description="Api自动化测试byZachTao", verbosity=2)
        runner.run(suite)
