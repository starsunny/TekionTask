#!/usr/bin/env python
from os import system
from commands import getstatusoutput
from time import sleep
import subprocess

Disconect=("grep 'Disconnect' /var/log/auth.log | awk '{print $11,$9}' | uniq -c ")
result=str(subprocess.check_output(Disconect, shell=True))
d=result.split(" ")
count=d[5]

def Dis(client) :
                client.send("dialog --msgbox \"How many times User disconnect ssh connection?\n" + count + "\n  \"   10 50")                

