import os
print "-----------------------------------------------\n\r"
print "-------CUSTOM SHELL - BARRY BURKE -C13427078\n\r"
print "------- GIVE US FULL MAKRS THERE -----------\n\r"

allowedCmds ={"pw":"pwcmd","ifc":"ifccmd","ud":"udcmd","dt":"datecmd"}


def pwcmd(options):
        print "pwd"


def datecmd(options):
        print "in date cmd"


def ifccmd(options):
        if len(options)>1:
                print "ifconfig {0}".format(options[1])
        else:
                print "ifconfig eth0"



def udcmd(options):
        print "in udcmd"

while (1==1):
        UserInput = raw_input('>')
        options = UserInput.split(' ')
        for key, value in allowedCmds.iteritems():
                if options[0] == key:
                        print "fxn going to be called {0}".format(key)
                        eval(value +"({0})".format(options))



