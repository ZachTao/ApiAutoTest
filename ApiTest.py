# -*-coding:utf-8 -*-
import unittest
from DealParam import ApiRequest
import HTMLTestRunner
import time
import os
'''
 # addTest 单独添加测试用例，内容为：类名（“方法名”）；
    # Test2是要测试的类名，test_one是要执行的测试方法
    # 执行其余的方法直接依照添加
    # suite.addTest(Test2("test_two"))
    # suite.addTest(Test2("test_one"))
    _____________________________________
    # addTests 是将需要执行的测试用例放到一个list后，再进行add，addTests 格式为：addTests(用例list名称)；
    tests = [Test2("test_two"), Test2("test_one")]
    suite.addTests(tests)
'''


class ApiTest(unittest.TestCase):

    def test_A(self):
        fpath = (r'/home/zach/pystore/PycharmProjects/ApiAutoTest/case_excel/ApiData.xls')
        ta = ApiRequest()
        ta.getpms_req(fpath)


if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    # suite.addTest(ApiTest('test_A'))
    # suite.addTests([ApiTest('test_A')])
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(ApiTest))
    # runner = unittest.TextTestRunner()
    now = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())
    cur_path = os.path.dirname(os.path.realpath(__file__))
    file_name = os.path.join(cur_path, "resultC") + "/" + now + "-report.html"
    fp = open(file_name, 'wb')
    # 定义报告格式
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='规范性检查测试报告',
        description=u'用例执行情况:')
    runner.run(suite)
    # 运行测试用例
    fp.close()
    # 关闭报告文件

