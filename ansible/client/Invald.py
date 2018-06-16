#!/usr/bin/env python
from os import system
from commands import getstatusoutput
from time import sleep
import subprocess


Invald=("grep 'Invalid' /var/log/auth.log | awk '{print $11,$9}' | uniq -c ")
result=str(subprocess.check_output(Invald, shell=True))
i=result.split(" ")
cnt=i[5]
iadr=i[6]
u=i[7]
#x= "(count1 + "Times" + Usr + "User")"
def In(client) :
                #client.send("recieve only")
                client.send("dialog --msgbox \" Invalid user....\" 6 30")

