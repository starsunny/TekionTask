#/usr/bin/python

import socket
from os import system
from commands import getstatusoutput
from time import sleep

ob = socket.socket()
ip = str("172.31.61.102")
ob.bind((ip,14012))
ob.listen(10)
client,addr = ob.accept()
client.send("dialog --infobox \"  Welcome to Linux Automation \n *****************************\" 5 35")
sleep (1)
import menu
menu.menu(client)
raw_input()
