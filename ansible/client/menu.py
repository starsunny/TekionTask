#!/usr/bin/env python
from os import system
from commands import getstatusoutput


def menu(client) :
	while True :	
		client.send("dialog --menu \"Select your requirement\" 15 30 4 1 \"Succesful User\" 2 \"Disconnected User\" 3 \"Invalid User\" ")
		choice = client.recv(10)

		if choice == "1" :   
			import Succes
			Succes.Success(client)
		elif choice == "2" : 
			import Disconnected
			Disconnected.Dis(client)
		elif choice == "3" : 
			import Invalid
			Invalid.In(client)
