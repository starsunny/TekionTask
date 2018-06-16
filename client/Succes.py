#!/usr/bin/env python
from os import system
from commands import getstatusoutput
from time import sleep
import subprocess

Succes=("grep 'Accepted' /var/log/auth.log | awk '{print $11,$9}' | uniq -c ")
result=str(subprocess.check_output(Succes, shell=True))
s=result.split(" ")
count1=s[5]
IPa=s[6]
Usr=s[7]

def Success(client) :
                #client.send("dialog --msgbox \"      IP \n" + IPa + "\n \" Times \" \n" + count1 + "\n \" User \"\n" + Usr + "\n \"   20 50")
                #client.send("dialog --msgbox \" IP \n" + IPa + "\n \n" + count1 + "\n \n" + Usr + "\n \"   20 50")
                client.send("dialog --msgbox \"How many times?\n" + count1 + "\nWhich User?\n" + Usr + "\n  \"   10 50")
                #client.send("dialog --msgbox \"    Count      IP    User\n" + result + "\n \"   10 50")
