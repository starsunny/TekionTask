#!/usr/bin/env python
from os import system
from commands import getstatusoutput
from time import sleep
import subprocess

Disconect=("grep 'Disconnect' /var/log/auth.log | awk '{print $11,$9}' | uniq -c ")
result=str(subprocess.check_output(Disconect, shell=True))
d=result.split(" ")
count=d[6]
IP=d[7]
User=d[8]
#x= "(count1 + "Times" + Usr + "User")"

def Dis(client) :
                #client.send("recieve only")
                client.send("dialog --msgbox \"No. '${count1}' IP '${IPa}' User '${Usr}'\"  6 30")

