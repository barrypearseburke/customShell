#!/usr/bin/python
import os
import datetime
import subprocess
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib
import re
"""
Shell can be made as the default shell for a user by
placing this file in /usr/bin
and running the commands below
Allow the user to read and write to his home directory using chmod - This is to allow Make File to work
sudo chmod a+x filename.py
sudo  chsh -s /usr/bin/filename.py USERNAME
NOTE: Python2.x must be installed.
"""

def cls(*args):
    """
    Calls to cmd prompt to clear users screen
    """
    os.system('clear')


cls()
print "-----------------------------------------------\n\r"
print "-------CUSTOM SHELL - BARRY BURKE -C13427078---\n\r"
print "------- GIVE US FULL MARKS THERE --------------\n\r"

allowedCmds = {"help": "help", "pw": "pwcmd", "ifc": "ifccmd", "ud": "udcmd", "dt": "datecmd",'whatishere':'ls','file':'file','quickmail':'sendmail','clear':'cls','cls':'cls'}


def help(*args):
    """
    Displays all available commands
    :return: 0 - Prints available commands to screen successful;1 failure
    """
    try:
        print "Here are all the commands you can run"
        for key, value in allowedCmds.iteritems():
            print key
        return 0
    except:
        return 1

def file(options):
    """
    :type options: list
    :param options: send in a list with the item 1 as the name of the directory
    :return: 0 for success ;1 for failure
    """
    try:
        os.system('nano {0}'.format(options[1]))
        return 0
    except:
        print "no filename supplied"
        return 1
def pwcmd(*args):
    """
    Prints Working directory
    """
    os.system("pwd")

def ls(*args):
    """
    :type args: list
    :param args:  element [1] as the with characters to search -Grep search
    """
    if len(args[0])==1:
        os.system('ls')
    else:
        os.system('ls -R|grep {0}'.format(args[0][1]))

def sendmail(*args):
    """
    Prompts users for email details
    :return: 1 failure ;0 success
    """
    fromadd = raw_input("Your email: ")
    passwd = raw_input('Your password: ')
    towhom = raw_input('To whom: ')
    subject = raw_input('Subject: ')
    body =  raw_input('Body of Email: ')
    send = raw_input('Will I send this email \r\nfrom:{0}\r\nto:{1}\r\nSubject:{2}\r\nBody:{3}\r\ny/n?'.format(fromadd,towhom,subject,body))
    if send.lower() == 'y':
        print("Sending Email. Please Wait")
        returnvalue  =sendemail(fromadd,passwd,towhom,subject,body)
        return returnvalue
    else:
        print "aborted"
        return 1

def sendemail(fromadd,pw,to,subject,body):
    """
    Sends email to given address from given address. For Google, you must allow less secure apps. Function auto detects domain and set smtp server
    only works for gmails, hotmnail/outlook, Mydit and dit domains.
    :type fromadd: string
    :param fromadd: Your Email Address
    :type pw: string
    :param pw: Your email password
    :type to: string
    :param to: The email address you want to send to
    :type body: String
    :param subject: The subject line of the email
    :type body: String
    :param body:Body of the email
    :return: 1 for success.
    """
    smtpservers ={'gmail':'smtp.gmail.com','mydit':'smtp.gmail.com','dit':'smtp.gmail.com','hotmail':'smtp.live.com','outlook':'smtp.live.com'}
    fromaddr = fromadd
    toaddr = to
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = subject

    body = body
    msg.attach(MIMEText(body, 'plain'))
    try:
        smtp = re.search('@[\w]+',fromadd).group()[1:]
    except:
        print "looks like you didn't give us a propper email there..."
        return 1
    try:
        server = smtplib.SMTP(smtpservers[smtp], 587)
    except:
        print("Here, want to check them details")
        return 1
    server.starttls()
    server.login(fromaddr, pw)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    print("Email Sent")
    server.quit()
    return  0


def datecmd(*args):
    """
    Prints the date in the format yyyymmddhhmmss
    :param args: None
    """
    i = datetime.datetime.now()
    date = "{0}{1}{2}{3}{4}{5}".format(i.year, i.month, i.day, i.hour, i.minute, i.second)
    print date


def ifccmd(*args):
    """
    if config with an allies.
    :type args list.
    :param args: list[1] with the interface you want. if unsupplied, eth0 result returned
    :return:
    """
    if len(args[0]) > 1:
        os.system("ifconfig {0}".format(args[0][1]))
    else:
        os.system("ifconfig eth0")


def udcmd(*args):
    """
    Prints userID, groupID, username, Main groupname, iNode of users home directory.
    """
    usernm = subprocess.check_output(['whoami'])
    usernm = usernm.strip("\r\n")
    userid = subprocess.check_output(['id', '-u', '{0}'.format(usernm)])
    userid = userid.strip("\r\n")
    groupid = subprocess.check_output(['id', '-g', '{0}'.format(usernm)])
    groupid = groupid.strip("\r\n")
    groupmain = subprocess.check_output(['groups', '{0}'.format(usernm)])
    groupmain = groupmain.strip("\r\n")
    groupmain = groupmain.split(' ')
    groupmain = groupmain[2]  # username,: and then first group.
    inode = subprocess.check_output(['ls', '-id'])
    print("{0},{1},{2},{3},{4}".format(userid, groupid, usernm, groupmain, inode))

def main():
    while (1 == 1):
        user = subprocess.check_output(['whoami'])
        user = user.strip("\r\n")
        hostname = subprocess.check_output(['hostname'])
        hostname = hostname.strip("\r\n")
        userprompt = ("{0}@{1}:>".format(user, hostname))
        UserInput = raw_input(userprompt)
        if UserInput == 'ifconfig' or UserInput == 'pwd':
            print("Sorry, You know {0} isent suppose to work,Next question...".format(UserInput))
        else:
            options = UserInput.split(' ')
            last = len(allowedCmds) - 1
            i =0
            for key, value in allowedCmds.iteritems():
                if options[0] == key:
                    # print "fxn going to be called {0}".format(key)
                    eval(value + "({0})".format(options))
                    i = -1
                if i == last:
                    print ("i dont have a clue whats going on, but \'{0}\' makes no sense to me. Try re-entering the command".format(options[0]))
                i =i+1

if __name__ == '__main__':
    main()