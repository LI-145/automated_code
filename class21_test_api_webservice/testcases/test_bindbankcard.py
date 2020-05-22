"""
=============================
Author  : lsw
Time    : 2019-09-20
E-mail  :591271859@qq.com
=============================
"""
import os
import time
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
class BankCardTestCase(unittest.TestCase):
    """绑定银行卡接口"""
    excel = ReadExcel(os.path.join(DATA_DIR, 'cases.xlsx'), 'bankcard')
    cases = excel.read_data_obj()
    db = ReadSQL()
    r_var = RandomeVar()
    web_s = WebRequests()

    def setUp(self):
        # 前置条件1：发送验证码
        url = myconf.get('url', 'test_url') + '/sms-service-war-1.0/ws/smsFacade.ws?wsdl'
        ip = self.r_var.random_ip()
        log.info("随机生成的IP：{}".format(ip))
        phone = self.r_var.random_phone()
        log.info("随机生成的手机号：{}".format(phone))

        data = {"client_ip": ip, "tmpl_id": 1, "mobile": phone}
        log.info("请求数据：{}".format(data))
        response1 = self.web_s.requests(url=url, interface="sendMCode", data=data)
        log.info("请求返回结果：{}".format(response1))
        db_no = phone[-2:]
        info_no = phone[-3]
        code = self.db.find_data(
            "SELECT Fverify_code FROM sms_db_{0}.t_mvcode_info_{1} WHERE Fmobile_no='{2}'".format(db_no, info_no,
                                                                                                  phone), res_num=1)
        log.info("{0}接收到的验证码为：{1}".format(phone, code[0]))
        setattr(ConText, 'phone', phone)

        # 前置条件2：注册新用户
        url = myconf.get('url', 'test_url') + '/finance-user_info-war-1.0/ws/financeUserInfoFacade.ws?wsdl'
        user = self.r_var.random_user()
        log.info("随机生成的用户名：{}".format(user))

        data = {"verify_code": code[0], "user_id": user, "channel_id": "1", "pwd": "123456", "mobile": phone, "ip": ip}
        log.info("请求数据：{}".format(data))
        response2 = self.web_s.requests(url=url, interface="userRegister", data=data)
        log.info("请求返回结果：{}".format(response2))
        uid = self.db.find_data("SELECT Fuid FROM user_db.t_user_info WHERE Fuser_id ='{}'".format(user), res_num=1)
        log.info("{} 的UID：{}".format(phone, uid[0]))
        # 将查询出来的用户UID，保存为临时变量
        setattr(ConText, 'uid', uid[0])
        db_no = phone[-2:]
        info_no = phone[-3]
        bind_card_table = "user_db_{0}.t_bind_card_{1}".format(db_no, info_no)
        setattr(ConText, 'table', bind_card_table[0])

        # 前置条件3：实名认证
        name = self.r_var.random_name()
        log.info("随机生成姓名：{}".format(name))
        setattr(ConText, 'name', name[0])
        now = time.strftime('%Y%m%d', time.localtime(time.time()))
        id_num = self.r_var.random_idnum('19800101', now)
        log.info("随机生成身份证号：{}".format(id_num))
        setattr(ConText, 'id_num', id_num[0])

        data = {"uid": uid, "true_name": name, "cre_id": id_num}
        log.info("请求数据：{}".format(data))
        response3 = self.web_s.requests(url=url, interface="verifyUserAuth", data=data)
        log.info("请求返回结果：{}".format(response3))
        try:
            self.assertEqual({"retCode": "0", "retInfo": "ok"}, response3)
        except AssertionError as e:
            log.info("{}实名认证失败，无法进行银行卡绑定！".format(phone))
            log.exception(e)
            raise e

    @data(*cases)
    def test_case_bank_card(self, case):
        """绑定银行卡"""
        url = myconf.get('url', 'test_url') + case.url

        bank_card = self.r_var.random_bankcard()
        log.info("随机生成的银行卡号：{}".format(bank_card))
        case.data = case.data.replace('*bank_card*', bank_card)

        case.data = data_replace(case.data)
        log.info("请求数据：{}".format(case.data))
        response = self.web_s.requests(url=url, interface="bindBankCard", data=eval(case.data))
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
