"""
=============================
Author  : lsw
Time    : 2019-09-02
E-mail  :591271859@qq.com
=============================
"""
import os

# 项目目录路径
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# 测试用例所在的目录路径
CASES_DIR = os.path.join(BASE_DIR, 'testcases')

# 测试报告所在的目录路径
REPORT_DIR = os.path.join(BASE_DIR, 'reports')

# 日志文件所在的目录路径
LOG_DIR = os.path.join(BASE_DIR, 'logs')

# 配置文件所在的目录路径
CONF_DIR = os.path.join(BASE_DIR, 'conf')

# 用例数据错在的目录路径
DATA_DIR = os.path.join(BASE_DIR, 'data')
