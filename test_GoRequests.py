# -*-coding:utf-8 -*-
import unittest
import time
import requests
from parameterized import parameterized
from DealParam import DealParams
from imporfile.HTMLTestRunnerNew import HTMLTestRunner
# from HTMLTestRunner_PY3 import HTMLTestRunner
# from imporfile.HTMLTestRunner import HTMLTestRunner
from logpri import MyLogging
from SendEmail import SendEmail
from ReadConfig import GetIni
import logging

flpath = r'F:\PycharmProjects\ApiAutoTest\case_excel\ApiData.xls'
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
                log.info("请求参数：%s" % regparams)
                log.info("请求地址：%s" % requrl)
                results = requests.post(requrl, regparams)
                log.info("返回结果：%s" % results)
                log.info("返回参数：%s" % results.text)
                response = results.status_code
                self.assertIn(response, [200], msg='返回reason不一致，测试不通过')
            elif reqmethod == ("get" or "GET"):
                log.info("请求参数：%s" % regparams)
                log.info("请求地址：%s" % requrl)
                results = requests.get(requrl, regparams)
                log.info("返回结果：%s" % results)
                log.info("返回参数：%s" % results.text)
                response = results.status_code
                self.assertIn(response, [200], msg='返回reason不一致，测试不通过')
            elif reqmethod == "put":
                log.info("请求参数：%s" % regparams)
                log.info("请求地址：%s" % requrl)
                results = requests.put(requrl, regparams)
                log.info("返回结果：%s" % results)
                log.info("返回参数：%s" % results.text)
                response = results.status_code
                self.assertIn(response, [200], msg='返回reason不一致，测试不通过')
            elif reqmethod == "patch":
                log.info("请求参数：%s" % regparams)
                log.info("请求地址：%s" % requrl)
                results = requests.patch(requrl, regparams)
                log.info("返回结果：%s" % results)
                log.info("返回参数：%s" % results.text)
                response = results.status_code
                self.assertIn(response, [200], msg='返回reason不一致，测试不通过')
            # elif reqmethod == "options":
            #     results = requests.options(requrl, headers=headers)
            # elif reqmethod == "delete":
            #     results = requests.delete(requrl, headers=headers)
            else:
                print('请求方法错误，请检查测试用例method数据')
        except Exception as e:
            # logging.error("service is error", e)
            log.info('接口调用出现异常了：%s' % e)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(GoRequests))
    now = time.strftime('%Y-%m-%d %H_%M_%S')
    report_path = r"F:\PycharmProjects\ApiAutoTest\HtmlRunnerResultC/"+now+"ApiTestReport.html"
    with open(report_path, "wb") as f:
        runner = HTMLTestRunner(stream=f, title="ApiTestReport", description="API自动化测试byZachTao", verbosity=2)
        runner.run(suite)
    time.sleep(5)
    a = GetIni()
    b = a.get_email_ini()
    s = SendEmail(b[0], b[1], b[2], b[3], b[4], b[5])
    s.log_in()
    print('邮件已发送！')
