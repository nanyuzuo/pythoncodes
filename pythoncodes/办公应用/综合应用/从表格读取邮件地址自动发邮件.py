# TODO 使用import导入smtplib模块
import smtplib
# 使用from..import导入邮件正文内容数据处理模块
from email.mime.text import MIMEText
# 使用from..import邮件协议的协议头模块
from email.header import Header
# TODO 使用import导入openpyxl模块
import openpyxl

# 邮箱服务器设置，赋值给mailHost
mailHost = "smtp.qq.com"
# 邮箱账号设置，赋值给mailUser
mailUser = "ahuayequ@qq.com"
# 邮箱授权码设置赋值给mailPass 
mailPass = "wiscbwlrcodprabd"

# 读取"/Users/ahua/汇总.xlsx"路径下的工作簿
wb = openpyxl.load_workbook("/Users/ahua/汇总.xlsx")
# 读取"面试教师名单"工作表，赋值给nameSheet
nameSheet = wb["面试教师名单"]
# 定义一个字典用于存储教师邮箱，赋值给teacherMail
teacherMail = {}

# 循环查找获取邮箱，追加到邮箱中
for rowData in nameSheet.rows:
    # 取每行第1个数据姓名赋值给name
    name = rowData[0].value
    # 取每行第11个数据邮箱赋值给mail
    mail = rowData[10].value
    # 按照name:mail的方式写入字典中
    teacherMail[name] = mail

# TODO 使用smtplib.SMTP_SSL(服务器, 端口号),端口号为465，赋值给smtpObj
smtpObj = smtplib.SMTP_SSL(mailHost,465)
# TODO 使用login()函数传入邮箱账户和授权码，登录邮箱
smtpObj.login(mailUser,mailPass)

# 将发送者邮箱赋值给sender
sender = mailUser

# TODO 将字典转换成可遍历的列表，并赋值给receiverList
receiverList = teacherMail.items()

# 遍历receiverList
for item in receiverList:
    # TODO 取第一个元素也就是姓名赋值给变量name
    name = item[0]
    # TODO 取第二个元素也就是收件人邮箱给变量receiver
    receiver = item[1]
    # 判断当变量name等于"姓名"时
    if name == "姓名":
        # 跳过本次循环
        continue
    # TODO 邮件正文：xx老师您好，恭喜您通过夜曲大学的筛选，现邀请您参加面试
    message = MIMEText(f"{name}老师您好，恭喜您通过夜曲大学的筛选，现邀请您参加面试", "plain", "utf-8")
    # TODO 邮件主题：夜曲大学面试邀请通知
    message["Subject"] = Header("夜曲大学面试邀请通知")
    # TODO 邮件发件人名称：夜曲大学教务处 <发件人邮箱地址>
    message["From"] = Header(f"夜曲大学教务处 <{sender}>")
    # TODO 邮件收件人名称：xx老师 <收件人邮箱地址>
    message["To"] = Header(f"{name}老师 <{receiver}>")
    # TODO 使用sendmail(发送人，收件人，message.as_string())发邮件
    smtpObj.sendmail(sender, receiver, message.as_string())
    # 获取姓名输出“xx邮件发送成功”
    print(f"{name}邮件发送成功")