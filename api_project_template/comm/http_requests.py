"""
=============================
Author  : lsw
Time    : 2019-10-16
E-mail  : 591271859@qq.com
=============================
"""
import requests


class HTTPRequest(object):
    """
    直接发送请求不记录cookies信息
    """
    def request(self, method, url, data=None, headers=None):
        method = method.lower()
        if method == 'post':
            return requests.post(url=url, data=data, headers=headers)
        elif method == 'get':
            return requests.get(url=url, params=data, headers=headers)


class HTTPSession(object):
    """
    使用session对象发送请求，自动记录cookies信息
    """
    def __init__(self):
        # 创建一个session对象
        self.session = requests.session()

    def request(self, method, url, data=None, headers=None):
        method = method.lower()
        if method == 'post':
            return self.session.post(url=url, data=data, headers=headers)
        elif method == 'get':
            return self.session.get(url=url, params=data, headers=headers)

    def close(self):
        self.session.close()