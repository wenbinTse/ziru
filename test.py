# -*- coding: utf-8 -*-
import requests
import re
import time

import smtplib
from email.mime.text import MIMEText
from email.header import Header

id = '62739'
url = 'http://www.ziroom.com/z/vr/' + id + '.html'

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent}

while True:
  print('循环中')
  res = requests.get(url, headers=headers)
  print(res.reason)
  pattern = re.compile(r'loading.jpg')
  result = re.findall(pattern, res.text)

  if len(result) == 0:
    print('可预订')
    sender = '1105268437@qq.com'
    receivers = ['1105268437@qq.com', 'yangj_96@126.com']

    mail_host="smtp.qq.com"  #设置服务器
    mail_user="1105268437"    #用户名
    mail_pass="***"   #口令 

    message = MIMEText(url + ' 可预订了', 'plain', 'utf-8')

    message['From'] = Header("谢文彬", 'utf-8')   # 发送者
    message['To'] =  Header("谢", 'utf-8')
    message['Subject'] = Header('房子', 'utf-8')

    smtpObj = smtplib.SMTP() 
    smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
    smtpObj.login(mail_user,mail_pass)
    try:  
      smtpObj.sendmail(sender, receivers, message.as_string())
      print("邮件发送成功")
    except smtplib.SMTPException:
      print("Error: 无法发送邮件")
    break
  else:
    print('配置中')
    time.sleep(30)


  
