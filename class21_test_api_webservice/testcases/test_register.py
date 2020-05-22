"""
=============================
Author  : lsw
Time    : 2019-09-19
E-mail  :591271859@qq.com
=============================
"""
import os
import unittest
from class21_test_api_webservice.common.mylogger import log
from class21_test_api_webservice.common.config import myconf
from class21_test_api_webservice.pack_lib.ddt import ddt, data
from class21_test_api_webservice.common.do_mysql import ReadSQL
from class21_test_api_webservice.common.constant import DATA_DIR
from class21_test_api_webservice.common.read_excel import ReadExcel
from class21_test_api_webservice.common.random_var import RandomeVar
from class21_test_api_webservice.common.web_requests import WebRequests
from class21_test_api_webservice.common.text_replace import data_replace, ConText


@ddt
class RegisterTestCase(unittest.TestCase):
    """用户注册接口"""
    excel = ReadExcel(os.path.join(DATA_DIR, 'cases.xlsx'), 'register')
    cases = excel.read_data_obj()
    db = ReadSQL()
    r_var = RandomeVar()
    web_s = WebRequests()

    def setUp(self):
        # 前置条件：发送验证码
        url = myconf.get('url', 'test_url') + '/sms-service-war-1.0/ws/smsFacade.ws?wsdl'
        ip = self.r_var.random_ip()
        log.info("随机生成的IP：{}".format(ip))
        phone = self.r_var.random_phone()
        log.info("随机生成的手机号：{}".format(phone))

        data = {"client_ip": ip, "tmpl_id": 1, "mobile": phone}
        log.info("请求数据：{}".format(data))
        response = self.web_s.requests(url=url, interface="sendMCode", data=data)
        log.info("请求返回结果：{}".format(response))

        db_no = phone[-2:]
        info_no = phone[-3]
        code = self.db.find_data(
            "SELECT Fverify_code FROM sms_db_{0}.t_mvcode_info_{1} WHERE Fmobile_no='{2}'".format(db_no, info_no,
                                                                                                  phone), res_num=1)
        log.info("{0}接收到的验证码为：{1}".format(phone, code[0]))
        # 将发送的验证码，保存为临时变量
        setattr(ConText, 'code', code[0])
        try:
            self.assertEqual({"retCode": "0", "retInfo": "ok"}, response)
        except AssertionError as e:
            log.info("{}发送验证码失败！".format(phone))
            log.exception(e)
            raise e

    @data(*cases)
    def test_case_register(self, case):
        """注册"""
        url = myconf.get('url', 'test_url') + case.url

        ip = self.r_var.random_ip()
        log.info("随机生成的IP：{}".format(ip))
        case.data = case.data.replace("*ip*", ip)
        phone = self.r_var.random_phone()
        log.info("随机生成的手机号：{}".format(phone))
        case.data = case.data.replace("*phone*", phone)
        user = self.r_var.random_user()
        log.info("随机生成的用户名：{}".format(user))
        case.data = case.data.replace("*user*", user)

        case.data = data_replace(case.data)
        log.info("请求数据：{}".format(case.data))
        response = self.web_s.requests(url=url, interface="userRegister", data=eval(case.data))
        log.info("请求返回结果：{}".format(response))

        try:
            self.assertEqual(eval(case.excepted), response)
            if case.check_sql:
                case.check_sql = data_replace(case.check_sql)
                log.info("请求数据库数据：{}".format(case.check_sql))
                db_res = self.db.find_count(case.check_sql)
                self.assertEqual(1, db_res)
        except AssertionError as e:
            self.excel.write_data(row=case.case_id + 1, column=7, value="未通过")
            log.info('{},该条测试用例执行未通过！'.format(case.title))
            log.exception(e)
            raise e
        else:
            self.excel.write_data(row=case.case_id + 1, column=7, value="通过")
            log.info('{},该条测试用例执行通过！'.format(case.title))

