"""
=============================
Author  : lsw
Time    : 2019-10-16
E-mail  : 591271859@qq.com
=============================
"""
import pymysql
from comm.config import myconf


class OperateSQL(object):
    """
    操作mysql
    """
    def __init__(self):
        self.conn = pymysql.connect(host=myconf.get('mysql', 'host'),
                                    port=myconf.getint('mysql', 'port'),
                                    user=myconf.get('mysql', 'user'),
                                    password=myconf.get('mysql','password'),
                                    database=myconf.get('mysql', 'database'),
                                    charset='utf8'
                                    )
        self.cur = self.conn.cursor()

    def find_data(self, sql, res_num=0):
        """
        查询数据
        :param sql: sql语句
        :param res_num: 默认为0，接收全部的返回结果，
                             为1，接收返回一个结果(第一个)
                             否则，接收返回res_num个结果
        :return: sql语句查询到的所有结果
        """
        self.conn.commit()
        self.cur.execute(sql)
        if res_num == 0:
            return self.cur.fetchall()
        elif res_num == 1:
            return self.cur.fetchone()
        else:
            return self.cur.fetchmany(res_num)

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
        """
        关闭游标及数据库
        :return: 无返回
        """
        self.cur.close()
        self.conn.close()
