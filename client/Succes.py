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

#x= "(count1 + "Times" + Usr + "User")"

#Controller Function 1 
def Success(client) :			
               # client.send("Got it")					
		client.send("dialog --infobox \"Details should be here\" 07 16")
		#client.send("recieve only")


#return
