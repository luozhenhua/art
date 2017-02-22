#!/usr/bin/env python
#
# This is the class to define DUT
#

import pexpect

class Target():

    def __init__(self, host, user, pwd):
        self._host = host
        self._user = user
        self._pass = pwd
        self.ssh_newkey = 'Are you sure you want to continue connecting'

    def connect(self):
        p = pexpect.spawn('ssh %s@%s' % (self._user, self._host))
        i = p.expect([self.ssh_newkey, 'password:', pexpect.TIMEOUT], 1)
        if i == 0:
            print("The first time login.")
            p.sendline('yes')
            p.expect([self.ssh_newkey, 'password:', pexpect.EOF])
        elif i == 1:
            print ("Input the password.")
            p.sendline(self._pass)
        elif i == 2:
            pass

        print p.before
        print p.after

        i = pexpect.run("ls -l")
        print(i)

    def __del__(self):
        pass

