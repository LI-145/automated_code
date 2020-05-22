"""
=============================
Author  : lsw
Time    : 2019-10-16
E-mail  : 591271859@qq.com
=============================
"""
import re
from comm.config import myconf


class ConText(object):
    """
    用来临时保存接口之间以来参数的类
    """

def data_replace(data):
    """
    替换动态参数
    :param data: 需要替换参数的变量
    :return: 替换参数后的数据
    """
    while re.search(r'#(.+?)#', data):
        res = re.search(r'(.+?)', data)
        # 提取要替换的内容
        r_data =  res.group()
        # 获取要替换的字段
        key = res.group(1)
        try:
            # 去配置文件中读取对应的数据
            value = myconf.get('data', key)
        except:
            # 去ConText中读取对相应的数据
            value = getattr(ConText, key)
        # 进行替换
        data = re.sub(r_data, str(value), data)
    return data