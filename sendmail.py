#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import datetime
import re
from optparse import OptionParser
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import time
import pdb
import sys
import os
import commands
reload(sys)
sys.setdefaultencoding('utf8')

def mail_sender(mto=None,output=None,used=None):
    """send mail"""
    mime_obj = MIMEMultipart()



    #subject 为邮件主题，这部分内容可以自由编辑，注意拼接格式
    subject="【!!!已使用" + used + "%!!!】-171服务器 " + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    #body_txt为邮件正文，可根据需求做改动
    body_txt="\n" + "\n" + "\t" + "171服务器使用情况" + "\n" + "\n" + "文件系统        容量  已用  可用 已用% 挂载点" + "\n" + output + "\n" + "\t" + "\n\n\n\n\n\nBest Regads\n---------------------\nIT组"


    if body_txt is not None:
        body = MIMEText(body_txt,'plain', 'utf-8')
        mime_obj.attach(body)


    mime_obj['to'] = mto
    #邮件的发送者,可随意编写
    mime_obj['from'] = "IT_Admin@xxx.xx"
    mime_obj['subject'] = subject

    try:
        server = smtplib.SMTP()#选择邮件服务器的方式
        server.connect('smtp.xxxx.cn')#连接的发送服务器的地址
        server.login('xxxxxx@xxxxxx','xxxxx')#给一个带有密码的账号，这样后续的邮件都是以此账号发送出去的，用户看到的名字为上from声明处内容
        server.sendmail(mime_obj['from'], mime_obj['to'],mime_obj.as_string())
        server.quit()
        print '发送成功'
        return 0
    except Exception, e:
        print str(e)
        return 1    

if __name__ == '__main__':
    #使用df -h 命令获取服务器使用情况
    cmd="df -h |grep  ^/"
    output=commands.getstatusoutput(cmd)
    output=output[1]

    #获取根目录使用情况
    cmd_used="df -h |grep ' /$'|awk '{print $5}' |sed 's/%//g'"
    output_used=commands.getstatusoutput(cmd_used)
    output_used=output_used[1]

    #如果根目录使用超过90%就发送邮件通知，发送人这里可以配置，90%也可以根据需求修改
    if int(output_used) > 95:
        mail_sender(mto="xxxxxxx@xxx",output=output,used=output_used)
