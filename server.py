#!/bin/env python
import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#host_name = socket.gethostname() #To get the name of host
port_number = 50008
print "The name of local machine"
host= (socket.gethostbyname(socket.gethostname()))
host_port_pair = (host,port_number) #A tuple
print host_port_pair
sock.bind(host_port_pair) #Bind address to the socket

sock.listen(10)
conn_obj,addr = sock.accept()
while True:
	print "Got a connection from ",addr," => Thanks..."
	msg_from_client = conn_obj.recv(2048)
	if not msg_from_client:
		print "<...No Relpy...> "
	else:
		print "FROM CLIENT ===> ", msg_from_client
		# conn_obj.send("Thanks for your connection") 
		conn_obj.send(raw_input("TYPE A MESSAGE FOR CLIENT ==> "))
conn_obj.close()	
#Closing the socket
sock.close()

