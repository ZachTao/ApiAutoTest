# -*-coding:utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
import ReadConfig


class SendEmail:

    def __init__(self, fromm, to, cc, part, tittle, text, pw):
        self.fromm = fromm
        self.to = to
        self.cc = cc
        self.part = part
        self.tittle = tittle
        self.text = text
        self.pw = pw

    def log_in(self):
        server = smtplib.SMTP_SSL()
        server.connect('smtp.qq.com', 465)
        server.login(self.fromm, self.pw)
        try:
            server.sendmail(self.fromm, self.to, self.makedata())
        finally:
            server.quit()

    def makedata(self):
        # 邮件头
        message = MIMEMultipart()
        message['From'] = self.fromm  # 发送
        message['To'] = ",".join(self.to)  # 收件
        message['To'] = ",".join(self.cc)
        message['Subject'] = Header(self.tittle, 'utf-8')
        body = MIMEText(open(self.part, 'rb').read(), _subtype="html", _charset="utf-8")
        message.attach(MIMEText(self.text, 'plain', 'utf-8'))  # 邮件正文
        message.attach(body)  # 附件内容html格式显示在文本内容中
        # 构造附件
        att1 = MIMEText(open(self.part, 'rb').read(), 'base64', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        att1["Content-Disposition"] = "attachment;filename=" + self.part
        message.attach(att1)
        fulltext = message.as_string()
        return fulltext


if __name__ == '__main__':
    print('-------------start--------------')
    part_address = '/home/zach/pystore/PycharmProjects/ApiAutoTest/resultC/2021-09-01 17_26_29ApiTestReport.html'
    s = SendEmail('1628995607@qq.com', ['1742235136@qq.com', '429529484@qq.com'], ['kevintaoxxy@163.com'], part_address, '测试邮件', '测试邮件内容', 'vcthhoovrwzwbecc')
    s.log_in()
    print('邮件已发送！')




