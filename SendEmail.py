# -*-coding:utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
import os
from ReadConfig import GetIni


class SendEmail:

    def __init__(self, fromm, to, cc, tittle, pw, part):
        self.fromm = fromm
        self.to = to
        self.cc = cc
        self.tittle = tittle
        self.pw = pw
        self.part = part

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
        message.attach(body)  # 附件内容html格式显示在文本内容中
        # message.attach(MIMEText(self.text, 'plain', 'utf-8'))  # 邮件正文
        # 构造附件
        att1 = MIMEText(open(self.part, 'rb').read(), 'base64', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        att1["Content-Disposition"] = "attachment;filename=" + self.part
        message.attach(att1)
        fulltext = message.as_string()
        return fulltext


if __name__ == '__main__':
    a = GetIni()
    b = a.get_email_ini()
    s = SendEmail(b[0], b[1], b[2], b[3], b[4], b[5], b[6])
    s.log_in()
    print('邮件已发送！')




