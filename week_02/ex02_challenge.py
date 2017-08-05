#!/usr/bin/env python

import telnetlib
import time
import socket
import sys
import getpass
import future

class TelnetIOSConn():
    UNAME_PROMPT = "Username: "
    PWD_PROMPT = "Password:" 
    PAGING_CMD= "terminal length 0" 
    END_CMD = "end"
    EXIT_CMD = "exit"


    def __init__(self,host,user,passwd,port=23,timeout=6):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.port = port
        self.timeout = timeout 

        try:
            self.tn_con = telnetlib.Telnet(self.host, self.port, self.timeout)
        except socket.timeout:
            raise ValueError("Unable to connect to " + self.host + ":" + self.port)
        
        self.tn_con.read_until(TelnetIOSConn.UNAME_PROMPT)
        self.tn_con.write(self.user + '\n')
        self.tn_con.read_until(TelnetIOSConn.PWD_PROMPT)
        self.tn_con.write(self.passwd + '\n')
        self.tn_con.read_very_eager()
        self.send_command(TelnetIOSConn.PAGING_CMD)

    def send_command(self, cmd):
        '''
        Send a command down the telnet channel
        Return the response
        '''
        cmd = cmd.rstrip()
        self.tn_con.write(cmd + '\n')
        time.sleep(1)
        return self.tn_con.read_very_eager()


##Write a script that connects using telnet to the pynet-rtr1 router.
#tn_con.write("show ip int brief\n")
#cmd_output = tn_con.read_until("pynet-rtr1#")
#print(cmd_output)
##Execute the 'show ip int brief' command on the router and return the output.
if __name__ == "__main__":
    con1 = TelnetIOSConn('184.105.247.70','pyclass','88newclass')
    print(con1.send_command('show ip int brief'))
