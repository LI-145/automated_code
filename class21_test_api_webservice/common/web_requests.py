"""
=============================
Author  : lsw
Time    : 2019-09-19
E-mail  :591271859@qq.com
=============================
"""
import suds
from suds import client


class WebRequests(object):
    """发送webservice请求"""
    def requests(self, url, interface, data):

        self.wsc = client.Client(url)
        try:
            response = eval("self.wsc.service.{}({})".format(interface, data))
        except suds.WebFault as e:
            return dict(e.fault)
        else:
            return dict(response)



