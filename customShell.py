import os
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
        print "date +%Y%m%d%H%M%S"


def ifccmd(options):
        if len(options)>1:
                print "ifconfig {0}".format(options[1])
        else:
                print "ifconfig eth0"



def udcmd(options):
        print "in udcmd"

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



