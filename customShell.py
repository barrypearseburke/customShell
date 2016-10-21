#!usr/bin/python
import os
import datetime
import subprocess
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib
import re


def cls(options):
    os.system('clear')


cls(options=False)
print "-----------------------------------------------\n\r"
print "-------CUSTOM SHELL - BARRY BURKE -C13427078---\n\r"
print "------- GIVE US FULL MARKS THERE --------------\n\r"

allowedCmds = {"help": "help", "pw": "pwcmd", "ifc": "ifccmd", "ud": "udcmd", "dt": "datecmd",'whatishere':'ls','newfile':'newfile','Quickmail':'sendmail'}


def help(options):
    for key, value in allowedCmds.iteritems():
        print key

def newfile(options):
    os.system('nano {0}'.format(options[1]))

def pwcmd(options):
    os.system("pwd")

def ls(options):
    if options ==1:
        os.system('ls')
    else:
        os.system('ls -R|grep {0}'.format(options[1]))

def sendmail(options):
        fromadd = raw_input('Your email')
        passwd = raw_input('Your password')
        towhom = raw_input('To whom')
        subject = raw_input('Subject')
        body =  raw_input('body of email')
        send = raw_input('Will i send email \r\n from:{0}\r\n to:{1}\r\nSubject{2}\r\n{3} \r\n y/n'.format(fromadd,towhom,subject,body))
        if send.lower() == 'y':
            print("Sending Email. Please Wait")
            sendemail(fromadd,passwd,towhom,subject,body)
        else:
            print "aborted"
        return 0

def sendemail(fromadd,pw,to,subject,body):
    smtpservers ={'gmail':'smtp.gmail.com','mydit':'smtp.gmail.com','dit':'smtp.gmail.com','hotmail':'smtp.live.com','outlook':'smtp.live.com'}
    fromaddr = fromadd
    toaddr = to
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = subject

    body = body
    msg.attach(MIMEText(body, 'plain'))
    smtp = re.search('@[\w]+',fromadd).group()[1:]
    try:
        server = smtplib.SMTP(smtpservers[smtp], 587)
    except:
        raise "domain not found"
    server.starttls()
    server.login(fromaddr, pw)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    print("Email Sent")
    server.quit()


def datecmd(options):
    i = datetime.datetime.now()
    date = "{0}{1}{2}{3}{4}{5}".format(i.year, i.month, i.day, i.hour, i.minute, i.second)
    print date


def ifccmd(options):
    if len(options) > 1:
        os.system("ifconfig {0}".format(options[1]))
    else:
        os.system("ifconfig eth0")


def udcmd(options):
    usernm = subprocess.check_output(['whoami'])
    usernm = usernm.strip("\r\n")
    userid = subprocess.check_output(['id', '-u', '{0}'.format(usernm)])
    userid = userid.strip("\r\n")
    groupid = subprocess.check_output(['id', '-g', '{0}'.format(usernm)])
    groupid = groupid.strip("\r\n")
    groupmain = subprocess.check_output(['groups', '{0}'.format(usernm)])
    groupmain = groupmain.split(' ')
    groupmain = groupmain[2]  # username,: and then first group.
    inode = subprocess.check_output(['ls', '-id'])
    print("{0},{1},{2},{3},{4}".format(userid, groupid, usernm, groupmain, inode))


while (1 == 1):
    user = subprocess.check_output(['whoami'])
    user = user.strip("\r\n")
    hostname = subprocess.check_output(['hostname'])
    hostname = hostname.strip("\r\n")
    userprompt = ("{0}@{1}:>".format(user, hostname))
    UserInput = raw_input(userprompt)
    options = UserInput.split(' ')
    for key, value in allowedCmds.iteritems():
        if options[0] == key:
            # print "fxn going to be called {0}".format(key)
            eval(value + "({0})".format(options))
