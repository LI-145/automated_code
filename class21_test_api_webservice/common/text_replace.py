"""
=============================
Author  : lsw
Time    : 2019-09-09
E-mail  :591271859@qq.com
=============================
"""
import re
from class21_test_api_webservice.common.config import myconf


class ConText(object):
    """用来临时保存接口之间依赖参数的类"""


def data_replace(data):
    """替换动态参数"""
    while re.search(r'#(.+?)#', data):
        res = re.search(r'#(.+?)#', data)
        # 提取要替换的内容
        r_data = res.group()
        # 获取要替换的字段
        key = res.group(1)
        # 去配置文件中读取字段对应的数据
        try:
            value = myconf.get('data', key)
        except:
            value = getattr(ConText, key)
        # 进行替换
        data = re.sub(r_data, str(value), data)
    return data


if __name__ == '__main__':
    pass


