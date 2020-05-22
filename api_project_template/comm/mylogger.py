"""
=============================
Author  : lsw
Time    : 2019-10-16
E-mail  : 591271859@qq.com
=============================
"""
import os
import logging
from comm.config import myconf
from comm.constant import LOG_DIR


class MyLogging(object):
    def __new__(cls, *args, **kwargs):
        # 创建日志收集器对象
        my_log = logging.getLogger('my_log')
        my_log.setLevel(myconf.get('log', 'log_level'))

        # 创建日志输出渠道
        # 输出到控制台
        sh = logging.StreamHandler()
        sh.setLevel(myconf.get('log', 's_level'))
        # 输出到文件
        fh = logging.FileHandler(os.path.join(LOG_DIR, myconf.get('log', 'filename')), encoding='utf8')
        fh.setLevel(myconf.get('log', 'f_level'))

        # 将日志收集器和输出渠道进行绑定
        my_log.addHandler(sh)
        my_log.addFilter(fh)
        # 指定日志输出格式
        fot = '%(asctime)s - [%(filename)s-->line:%(lineno)d] - %(levelname)s:%(message)s'
        # 创建日志格式对象
        formatter = logging.Formatter(fot)
        # 输出格式绑定到输出渠道(给输出渠道指定输出格式)
        sh.setFormatter(formatter)
        fh.setFormatter(formatter)
        # 将日志收集器进程返回
        return my_log

log = MyLogging()