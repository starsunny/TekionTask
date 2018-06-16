#!/usr/bin/env python
from os import system
from commands import getstatusoutput
from time import sleep
import subprocess


Invald=("grep 'Invalid' /var/log/auth.log | awk '{print $11,$9}' | uniq -c ")
result1=str(subprocess.check_output(Invald, shell=True))
i=result.split(" ")
cnt=i[6]
iadr=i[7]
u=i[8]
#x= "(count1 + "Times" + Usr + "User")"

#Controller Function 1 
def In(client) :			
               # client.send("Got it")					
		client.send("dialog --infobox \"Details should be here \" 07 16")
		#client.send("recieve only")


