# coding=utf-8
import smtplib
from email.mime.text import MIMEText
msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')

from_addr = raw_input('From: ')
password = raw_input('Password: ')
# 输入收件人地址:
to_addr = raw_input('To: ')
# 输入SMTP服务器地址:
smtp_server = raw_input('SMTP server: ')

server = smtplib.SMTP_SSL(smtp_server, 465) # SMTP协议默认端口是25
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, to_addr, msg.as_string())
server.quit()