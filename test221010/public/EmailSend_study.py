import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr
import sys
sys.path.append(r"E:\A_PythonProject\TestProject\test221010")
import zipfile
import os
class EmailSend:
    def __init__(self,dirpath,outFullName,fujian_name=None,):
        self.fujian_name = fujian_name
        self.dirpath = dirpath
        self.outFullName = outFullName
        #创建SMTP对象
        self.smtp = smtplib.SMTP()
        #连接指定服务器
        self.smtp.connect("smtp.126.com", port=25)
        #登录，使用邮箱和授权码
        self.smtp.login(user="zw958227254@126.com", password="IHUHLOVFEUYNFTPL")
    def smtpreturn(self):
        self.smtp
    def __mimetext(self,mimetext,fromtext,to,titlesubject):
        #构造MIMEText对象，参数为：正文，MIME的subtpe，编码方式
        message = MIMEText(mimetext, "plain", "utf-8")
        message['From'] = Header(fromtext, 'utf-8')#发件人昵称
        message['To'] = Header(to, 'utf-8')#收件人昵称
        message['Subject'] = Header(titlesubject, 'utf-8')#定义主体内容
        return message
    def __file_mimetext(self,fromtext,to,titlesubject):
        message = MIMEText(open(self.fujian_name,"rb").read(),"base64","utf-8")#文件流
        #message = MIMEText("请下载附件查看自动化测试报告", "plain", "utf-8")
        message["Content-Type"] = "application/ostet-stream" #类型
        message["Content-Disposition"] = "attachment; filename="+self.fujian_name #发送的附件文件名
        message['From'] = Header(fromtext, 'utf-8')  # 发件人昵称
        message['To'] = Header(to, 'utf-8')  # 收件人昵称
        message['Subject'] = Header(titlesubject, 'utf-8')  # 定义主体内容
        print(message)
        return message
    #print(message)
    def sendemail(self,addrs=['18407469853@163.com']):
        if self.fujian_name:
            message = self.__file_mimetext(to='你', fromtext='周伟', titlesubject="测试发送自动化测试报告")
        else:
            message = self.__mimetext(mimetext='发送给大佬的邮件', to='你', fromtext='周伟',titlesubject="测试发送自动化测试报告")

        print(message)
        self.smtp.sendmail(from_addr='zw958227254@126.com',to_addrs=addrs,msg=message.as_string())
        self.smtp.quit()

    def zipDir(self):
        zip = zipfile.ZipFile(self.outFullName,"w",zipfile.ZIP_DEFLATED)
        for path, dirnames, filenames in os.walk(self.dirpath):
            #去掉目标跟路径，只对目标文件夹下边的文件及文件夹进行雅俗
            fpath = path.replace(self.dirpath, '')
            for filename in filenames:
                zip.write(os.path.join(path, filename), os.path.join(fpath,filename))
        zip.close()
        print("压缩成功")
if __name__ == '__main__':
    # 判断是否存在，存在先删除
    if os.path.exists("send_dir.zip"):
        os.system("del -s -q send_dir.zip")
        print("删除zip成功")
    if os.path.exists("send_dir\\allure-report"):
        os.system("rmdir /s /q send_dir\\allure-report")
        print("删除report成功")
    #移动report
    try:
        os.system("move E:\A_PythonProject\TestProject\\allure-report send_dir")
        print("移动report到send_dir")
    except Exception as e:
        print(e)
    print("测试压缩附件")
    emailsend = EmailSend(r"send_dir",r"send_dir.zip",'send_dir.zip')
    # emailsend.zipDir()
    # emailsend.sendemail()
