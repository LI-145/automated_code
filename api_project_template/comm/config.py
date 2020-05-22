"""
=============================
Author  : lsw
Time    : 2019-10-16
E-mail  : 591271859@qq.com
=============================
"""
import os
from configparser import ConfigParser
from comm.constant import CONF_DIR


class MyConfig(ConfigParser):
    """
    读取配置文件的类
    """
    def __init__(self):
        super().__init__()
        # 初始化的时候，打开配置文件
        self.read(os.path.join(CONF_DIR, 'conf.ini'))

myconf = MyConfig()