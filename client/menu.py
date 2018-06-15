#!/usr/bin/python


from os import system
from commands import getstatusoutput


def menu(client) :
	while True :	
		client.send("dialog --menu \"Select your requirement\" 15 30 4  1 \"Succesful User\" 2 \"Disconnected User\" 3 \"Invalid User\" 8 \"Exit\" ")
                #choice = raw_input()
		choice = client.recv(2)

		if choice == "1" :   
			import Succes
			Succes.Success(client)
		elif choice == "2" : 
			import Disconnected
			dirs.dirs(client)
		elif choice == "3" : 
			import Invalid
			files.files(client)
		elif choice == "8" :
			client.recv("recieve only")
			client.recv("dialog --infobox \"Thank You... \n Exiting....\" 5 18")
			client.recv("false")


