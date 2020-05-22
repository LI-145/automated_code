"""
=============================
Author  : lsw
Time    : 2019-10-16
E-mail  : 591271859@qq.com
=============================
"""
import os

# 项目所在路径
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# 配置文件所在路径
CONF_DIR = os.path.join(BASE_DIR, 'conf')

# 用例数据所在路径
DATA_DIR = os.path.join(BASE_DIR, 'data')

# 日志所在路径
LOG_DIR = os.path.join(BASE_DIR, 'logs')

# 测试用例所在路径
CASE_DIR = os.path.join(BASE_DIR, 'testcases')

# 测试报告所在路径
REPORT_DIR = os.path.join(BASE_DIR, 'reports')

# 发送测试报告的邮箱账号及密码
MAIL_USER = "testlsw@163.com"
MIAL_PWD = "lisiweicheng524"