# -*-coding:utf-8 -*-
import unittest
import time
import requests
import logging
from parameterized import parameterized
from DealParam import DealParams
from HTMLTestRunner import HTMLTestRunner


class GoRequests(unittest.TestCase):
    # headers = {
    #     'User - Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
    #                     'Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.84'}
    # @parameterized.expand(DealParams())
    @parameterized.expand(['get', 'http://apis.juhe.cn/mobile/get', {'key': 'cbc373b0719df7a8e129b0128a5a94a4', 'dtype': 'json', 'phone': '19974865500.0'}])
    # 上面返回的参数需要是List
    def test_rego(self, reqmethod, requrl, regparams):
        print('----------run----------')
        try:
            if reqmethod == ("post" or "POST"):
                results = requests.post(requrl, regparams)
                print('-----------post------------')
            elif reqmethod == ("get" or "GET"):
                results = requests.get(requrl, regparams)
                print('-----------get------------')
            elif reqmethod == "put":
                results = requests.put(requrl, regparams)
            elif reqmethod == "patch":
                results = requests.patch(requrl, regparams)
            # elif reqmethod == "options":
            #     results = requests.options(requrl, headers=headers)
            # elif reqmethod == "delete":
            #     results = requests.delete(requrl, headers=headers)
            response = results.json()
            print(response)
            code = response.get("reason")
            print(code)
            return code
        except Exception as e:
            logging.error("service is error", e)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(GoRequests))
    now = time.strftime('%Y-%m-%d %H_%M_%S')
    report_path = r"/home/zach/pystore/PycharmProjects/ApiAutoTest/resultC/report.html"
    with open(report_path, "wb") as f:
        runner = HTMLTestRunner(stream=f, title="Esearch接口测试报告", description="测试用例执行情况", verbosity=2)
        runner.run(suite)
