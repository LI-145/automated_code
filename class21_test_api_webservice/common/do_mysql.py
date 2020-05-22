"""
=============================
Author  : lsw
Time    : 2019-09-04
E-mail  :591271859@qq.com
=============================
"""
import pymysql
from class21_test_api_webservice.common.config import myconf


class ReadSQL(object):
    """操作mysql"""
    def __init__(self):
        # 连接数据库
        self.conn = pymysql.connect(host=myconf.get('mysql', 'host'),
                                    port=myconf.getint('mysql', 'port'),
                                    user=myconf.get('mysql', 'user'),
                                    password=myconf.get('mysql', 'password'),
                                    charset='utf8'
                                    )
        # 创建一个游标
        self.cur = self.conn.cursor()

    def find_data(self, sql, res_num=0):
        """
        查询数据
        :param sql: sql语句
        :param res_num: 默认为0，接收全部的返回结果，
                             为1，接收返回一个结果(第一个)
        :return: sql语句查询到的所有结果
        """
        self.conn.commit()
        self.cur.execute(sql)
        if res_num == 0:
            return self.cur.fetchall()
        elif res_num == 1:
            return self.cur.fetchone()

    def find_count(self, sql):
        """
        查询数据返回的条数
        :param sql: sql语句
        :return: sql语句影响的数据条数
        """
        self.conn.commit()
        count = self.cur.execute(sql)
        return count

    def close(self):
        # 关闭游标
        self.cur.close()
        # 断开连接
        self.conn.close()
