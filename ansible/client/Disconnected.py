#!/usr/bin/env python
from os import system
from commands import getstatusoutput
from time import sleep
import subprocess

Disconect=("grep 'Disconnect' /var/log/auth.log | awk '{print $11,$9}' | uniq -c ")
result2=str(subprocess.check_output(Disconect, shell=True))
d=result.split(" ")
count=d[6]
IP=d[7]
User=d[8]
#x= "(count1 + "Times" + Usr + "User")"

#Controller Function 1 
def Dis(client) :			
               # client.send("Got it")					
		client.send("dialog --infobox \"Details should be here \" 07 16")
		#client.send("recieve only")
