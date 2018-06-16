#!/usr/bin/python


from os import system
from commands import getstatusoutput


def menu(client) :
	while True :	
		client.send("dialog --menu \"SSH login attempts\" 15 20 4  1 \"Successfull\" 2 \"Disconnect\" 3 \"Invalid\" 4 \"Exit\" ")
		choice = client.recv(10)

		if choice == "1" :   
			import Succes
			Succes.Success(client)
		elif choice == "2" : 
			import Disconnected
			Disconnected.Dis(client)
		elif choice == "3" : 
			import Invald
			Invald.In(client)
                elif choice == "4" :
			#client.send("recieve only")
			client.send("dialog --msgbox \"Thank You... \n Exiting....\" 5 18")
			client.send("false")
