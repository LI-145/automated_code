"""
=============================
Author  : lsw
Time    : 2019-09-02
E-mail  :591271859@qq.com
=============================
"""
import os
import time
import unittest
from HTMLTestRunnerNew import HTMLTestRunner
from class21_test_api_webservice.common.mylogger import log
from class21_test_api_webservice.common.constant import CASES_DIR, REPORT_DIR
from class21_test_api_webservice.testcases import test_sendcode, test_register,test_verifyauth,test_bindbankcard


log.info("--------------------测试用例开始执行--------------------")
# 创建测试套件
suit = unittest.TestSuite()

# 将用例添加到套件
loader = unittest.TestLoader()
# suit.addTest(loader.discover(CASES_DIR))
# suit.addTest(loader.loadTestsFromModule(test_sendcode))
# suit.addTest(loader.loadTestsFromModule(test_register))
# suit.addTest(loader.loadTestsFromModule(test_verifyauth))
suit.addTest(loader.loadTestsFromModule(test_bindbankcard))

# 测试报告名称
now = time.strftime("%Y%m%d%H%M%S")
report_name = now + 'test_report.html'

# 执行用例并生成测试报告
with open(os.path.join(REPORT_DIR, report_name), 'wb') as wo:
    runner = HTMLTestRunner(stream=wo,
                            verbosity=2,
                            title="python21接口项目",
                            description="python21项目实战",
                            tester="lsw"
                            )
    runner.run(suit)

log.info("--------------------测试用例执行完成--------------------")
