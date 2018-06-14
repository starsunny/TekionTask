#!/bin/env python
import os
import time
import commands
import socket
import sys, subprocess
#import sleep

'''
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host_name = socket.gethostname() #To get the name of host
port_number = 50008
print "The name of local machine" #The name of local machine admins-MacBook-Pro-3.local

host_port_pair = ('172.31.58.187',port_number) #A tuple

sock.connect(host_port_pair)  #To actively intiate the TCP Server connection

while True:

        print "TYPE A MESSAGE FOR SERVER ==> ",
        msg_for_server = raw_input()
        if not msg_for_server:
                break
        sock.send(msg_for_server)

        msg_from_server = sock.recv(2048)
        if not msg_from_server:
                print "<...No Reply from Server...>"
        else:
                print "From Server ==> ",msg_from_server

sock.close()

"""
        print type(sock.recv(2048)),sock.recv(2048)
"""
#HOST='34.204.3.76' #localhost
#PORT=50008
#host_name = socket.gethostname() #To get the name of host
#s=socket.socket(socket.AF_INET, socket.SOCK_STREAM ) #create an INET, STREAMing socket
#s.bind((host_name,PORT)) #bind to that port
#s.listen(10) #listen for user input and accept 1 connection at a time.
#conn, addr = s.accept()
#print "The connection has been set up"
#hostname = socket.gethostname()
#print "Connection succesful"
'''
host_name = socket.gethostname()

print "Loading....."
time.sleep (1)
print '''
                                                      SSH CONNECTIONS
                                        ---------------------------------------------
                                       | 1. Count of Successfull SSH users connected |
                                       | 2. Count of Invalid SSH user connections    |
                                       | 3. Count of Disconnected SSH users          |
                                        ---------------------------------------------
'''

choice=raw_input("Please Select your choice wisely: ")

Succes=("grep 'Accepted' /var/log/auth.log | awk '{print $11,$9}' | uniq -c ")
result=str(subprocess.check_output(Succes, shell=True))
s=result.split(" ")
#print s
#Usr=range(100)
count1=s[5]
IPa=s[6]
Usr=s[7]
#print s[8]

Invald=("grep 'Invalid' /var/log/auth.log | awk '{print $11,$9}' | uniq -c ")
result1=str(subprocess.check_output(Invald, shell=True))
i=result.split(" ")
s=result.split(" ")
count1=s[5]
IPa=s[6]
usr=s[7]

Disconect=("grep 'Disconnect' /var/log/auth.log | awk '{print $11,$9}' | uniq -c ")
result2=str(subprocess.check_output(Disconect, shell=True))
d=result.split(" ")
count=d[5]
IP=d[6]
User=d[7]

#time.sleep (1)
if choice == '1':
   print ('This IP'+ IPa +' and HostName '+ host_name +' has successfully logged in '+ count1 +' Times by user '+ Usr)
#print "-----------"
#time.sleep (1)
#print "-----------"
elif choice == '2':
   print ('This IP'+ iadr +' and HostName'+ hostname +' has Invalid logged in '+ cnt +' Times by user'+ usr)
#print "-----------"
#time.sleep (1)
#print "-----------"
elif choice == '3':
   print ('This IP'+ IP +' and HostName '+ hostname +' has disconnected '+ count +' Times by user'+ User)

else:
   print "Please enter the right choice : "

                                 
