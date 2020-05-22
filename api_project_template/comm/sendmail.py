"""
=============================
Author  : lsw
Time    : 2019-11-26
E-mail  : 591271859@qq.com
=============================
"""
import os
import smtplib
from comm.mylogger import log
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from comm.constant import REPORT_DIR,MAIL_USER,MIAL_PWD


class SendMail(object):

    def new_report(self):
        """查找最新的测试报告"""
        dirs = os.listdir(REPORT_DIR)
        dirs.sort()
        new_report_name = dirs[-1]
        print("最新的测试报告是：{}".format(new_report_name))
        file_new = os.path.join(REPORT_DIR,new_report_name)
        return file_new

    def send_mail(self,to_mail):
        """发送最新的测试报告到指定邮箱"""
        # 连接到smtp服务器
        smtp = smtplib.SMTP_SSL(host='smtp.163.com', port=465)
        # 登录smtp服务器
        smtp.login(MAIL_USER, MIAL_PWD)
        # 构建一封带附件的邮件
        # 创建一封多组件的邮件
        msg = MIMEMultipart()
        # 发件人
        msg['From'] = MAIL_USER
        # 收件人
        msg['To'] = to_mail
        # 主题
        msg['Subject'] = Header("接口自动化测试报告", 'utf8')
        # 添加附件
        self.file_new = self.new_report()
        f_msg = open(self.file_new, 'rb').read()
        msg_file = MIMEApplication(f_msg)
        msg_file.add_header('content-disposition','attachment',filename="TestReport.html")
        msg.attach(msg_file)
        # 正文
        text = MIMEText(f_msg, 'html', 'utf8')
        # 把邮件的文本内容添加到多组件的邮件中
        msg.attach(text)
        # 发送邮件
        smtp.send_message(msg=msg,from_addr=MAIL_USER,to_addrs=to_mail)
        smtp.quit()
        log.info("SENDMAIL SUCCESS！")




