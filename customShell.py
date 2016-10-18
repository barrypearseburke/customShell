import os
import datetime
import subprocess
print "-----------------------------------------------\n\r"
print "-------CUSTOM SHELL - BARRY BURKE -C13427078---\n\r"
print "------- GIVE US FULL MAKRS THERE --------------\n\r"

allowedCmds ={"help":"help","pw":"pwcmd","ifc":"ifccmd","ud":"udcmd","dt":"datecmd"}

def help(options):
    print("Available cmds {0}".format(key for key, value in allowedCmds.iteritems() ))
def pwcmd(options):
        print "pwd"


def datecmd(options):
        i = datetime.datetime.now()
        date = "{0}{1}{2}{3}{4}{5}".format(i.year,i.month,i.day,i.hour,i.minute,i.second)
        print date

def ifccmd(options):
        if len(options)>1:
                print "ifconfig {0}".format(options[1])
        else:
                print "ifconfig eth0"



def udcmd(options):
        usernm = subprocess.check_output(['whoami'])
        userid = subprocess.check_output(['id' '-u' '{0}'.format(usernm)])
        groupid = subprocess.check_output(['id','-g','{0}'.format(usernm)],shell=True)
        groupmain = subprocess.check_output(['groups', '{0}'.format(usernm)],shell=True)
        groupmain = groupmain.split(' ')
        groupmain = groupmain[0]
        inode = subprocess.check_output(['ls -id'])
        print (groupmain)
        print (inode)

while (1==1):
        user = subprocess.check_output(['whoami'])
        user=user.strip("\r\n")
        hostname = subprocess.check_output(['hostname'])
        hostname =hostname.strip("\r\n")
        userprompt = ("{0}@{1}:>".format(user,hostname))
        UserInput = raw_input(userprompt)
        options = UserInput.split(' ')
        for key, value in allowedCmds.iteritems():
                if options[0] == key:
                        print "fxn going to be called {0}".format(key)
                        eval(value +"({0})".format(options))



