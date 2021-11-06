import smtplib
from future.backports.email.header import Header
from future.backports.email.mime.text import MIMEText
from account_time import account_time
from remain import data
from remain import remain

# 发件人和收件人
sender = ' '
receiver = ' '
# 所使用的用来发送邮件的SMTP服务器
smtpServer = ' '
# 发送邮箱的用户名和授权码（不是登录邮箱的密码）
username = ' '
password = ' '
mail_title = ' '

start_school = " " # 开学时间
week = account_time.account_week(start_school)
day = account_time.account_day()
news = '\n'.join(remain.text(week, day, data))
mail_body = news

message = MIMEText(mail_body, 'plain', 'utf-8')  # 邮件正文
message['From'] = sender  # 邮件上显示的发件人
message['To'] = receiver  # 邮件上显示的收件人
message['Subject'] = Header(mail_title, 'utf-8')  # 邮件主题

try:
    smtp = smtplib.SMTP()  # 创建一个连接
    smtp.connect(smtpServer)  # 连接发送邮件的服务器
    smtp.login(username, password)  # 登录服务器
    smtp.sendmail(sender, receiver, message.as_string())  # 填入邮件的相关信息并发送
    print("邮件发送成功！！！")
    smtp.quit()
except smtplib.SMTPException:
    print("邮件发送失败！！！")
