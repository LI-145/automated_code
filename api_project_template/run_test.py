"""
=============================
Author  : lsw
Time    : 2019-10-16
E-mail  : 591271859@qq.com
=============================
"""
import os
import time
import unittest
from comm.mylogger import log
from HTMLTestRunnerNew import HTMLTestRunner
from comm.constant import CASE_DIR, REPORT_DIR


log.info("--------------------测试用例开始执行--------------------")
# 创建测试套件
suit = unittest.TestSuite()
# 将测试用例添加到套件
loader = unittest.TestLoader()
suit.addTest(loader.discover(CASE_DIR))

# 测试报告名称
now = time.strftime("%Y%m%d%H%M%S")
report_name = now + 'test_report.html'

# 执行测试用例并生成测试报告
with open(os.path.join(REPORT_DIR, report_name),'wb') as wo:
    runner = HTMLTestRunner(stream=wo,
                            verbosity=2,
                            title="python接口自动化项目报告",
                            description="python接口自动化项目模板",
                            tester="lsw"
                            )
    runner.run(suit)

log.info("--------------------测试用例执行完成--------------------")









