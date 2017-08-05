#!/usr/bin/env python
import telnetlib

#Write a script that connects using telnet to the pynet-rtr1 router.
tn_con = telnetlib.Telnet("184.105.247.70")
tn_con.read_until("Username: ")
tn_con.write("pyclass\n")
tn_con.read_until("Password: ")
tn_con.write("88newclass\n")
tn_con.read_until("pynet-rtr1#")
tn_con.write("show ip int brief\n")
cmd_output = tn_con.read_until("pynet-rtr1#")
print(cmd_output)
#Execute the 'show ip int brief' command on the router and return the output.
