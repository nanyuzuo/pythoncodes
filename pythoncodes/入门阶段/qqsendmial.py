import smtplib
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

qqMail = smtplib.SMTP_SSL("smtp.qq.com",465)
mailUser = "115185849@qq.com"
mailPass = "fsleaodwaiegbjea"
qqMail.login(mailUser,mailPass)
sender = "115185849@qq.com"
receiver = "nanyuzuo@163.com"
message = MIMEMultipart()
message["Subject"] = Header("团队合照")
message["From"] = Header(f"hooray<{sender}>")
message["To"] = Header(f"nanyuzuo<{receiver}>")

textContent = "请收好这张照片"
mailContent = MIMEText(textContent,"plain","utf-8")

filepath = r"d:\a.jpg"
with open(filepath,"rb") as imageFile:
    fileContent = imageFile.read()

attachment = MIMEImage(fileContent)
attachment.add_header("Content-Disposition","attachment",filename="a.jpg")   

message.attach(mailContent)
message.attach(attachment)

qqMail.sendmail(sender,receiver,message.as_string())
print("发送成功！")
