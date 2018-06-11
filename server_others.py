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
THREAD_STATUS = 1

BUFFER_SIZE = 1024

STATUS = 0
# 0 - no SOCKET
# 1 - created SOCKET, but no connectThread and no CONNECTS
# 2 - created SOCKET and connectThread, but no  no CONNECTS
# 3 - created SOCKET, connectThread, and have CONNECTS

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#	Commands for <User>
#
#	test
#	color none
#	color 1
#	exit
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def login(): # Сonfirmation
	global PASSWORT

	i = 0

	while i < 4:
		p = str(getpass("password: "))

		if p == PASSWORT:	
			return 1234
		print("Incorrect password.")
		i += 1

	print("Authorization completed unsuccessfully!")

def printInfo(): # Command <info>
	s = None
	if STATUS == 0:
		s = "No SOCKET!"
	elif STATUS == 1:
		s = "SOCKET created | No connectThread | No CONNECTS"
	elif STATUS == 2:
		s = "SOCKET created | connectThread created | No CONNECTS"
	elif STATUS == 3:
		s = "SOCKET created | connectThread created | CONNECTS = " + str(CONNECTS)
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
	print("BUFFER_SIZE sever`s:", BUFFER_SIZE)
	print()

def printHelp(): # Command <help>
	print()
	print("________Commands________")
	print("connect")
	print("info")
	print("help")
	print("list")
	print("connections")
	print("buffer")
	print("password")

def printList(): # Command <list>
	print()
	print("________List________")
	for number in range(CONNECTS):
		print(number, "|", address_list[number])

def printConnections(): # Command <connections>
	print()
	print("________Connections________")
	for number in range(CONNECTS):
		obj = connect_list[number]
		obj.send(str("test").encode('utf-8'))
		m = obj.recv(1024)

		m = m.decode("utf-8")

		if m == '0':
			User = '+'
		else:
			User = '-'
		print(number, "|", User)

def msgUser(msg): # msg != msg.decode("utf-8")
	msg = msg.decode("utf-8")

	if msg == '0': # Connected successfully!
		return "<Client> connected successfully!"
	elif msg == '1': # User doesn't know <Command>
		return "<Client> hat dich nicht versteht!"
	elif msg == '2': # Error user`s
		return "<Client> ERROR!"
	elif msg == '3': # User know <Command>
		return "<Client> understand you!"

class ConnectUsersThread(threading.Thread): # ConnectUsersThread
	def __init__(self):
		threading.Thread.__init__(self)
		self.daemon = True

	def run(self):
		global connect_list
		global address_list
		global CONNECTS
		global STATUS

		print("ConnectUsersThread created successfully!")

		while THREAD_STATUS == 1:
			connect , address = SOCKET.accept()
			connect_list.append(connect)
			address_list.append(address)

			CONNECTS += 1
			STATUS = 3

def connectCommand(): # Command <connect>
	global THREAD
	global STATUS

	THREAD = ConnectUsersThread()
	THREAD.start()

	STATUS = 2

def sendCommandAllUsers(msg): # msg != msg.encode("utf-8")
	print("________Send all <User>________")

	for number in range(CONNECTS):
		obj = connect_list[number]
		obj.send(msg.encode('utf-8'))
		m = obj.recv(1024)

		User = msgUser(m)

		print(number, "|", User)

def sendCommandOneUsers(msg, i): # msg != msg.encode("utf-8"), i = int(i)
	print("________Send", i, "<User>________")

	if i>=0 and i<CONNECTS:
		obj = connect_list[i]
		obj.send(msg.encode('utf-8'))
		m = obj.recv(1024)

		User = msgUser(m)

		print(i, "|", User)

def sendCommand(): # Command <send>
	print()
	print("Connected", CONNECTS, "users")

	if CONNECTS > 0:
		try:
			i = input("Enter number CONNECTS   (int or <all>)  : ")
		except EOFError:
			pass
		print()

		msg = str(input("Enter <command> for <User>: "))

		if str(i) == "all":
			sendCommandAllUsers(msg)
		else:
			try:
				sendCommandOneUsers(msg, int(i))
			except ValueError:
				print(i, "not number!")
			except EOFError:
				pass
	else:
		print("No CONNECTS!")

def bufferCommand(): # Command <buffer>
	global BUFFER_SIZE

	try:
		BUFFER_SIZE = int(input("Enter new BUFFER_SIZE: "))
	except Exception as TypeError:
		print(i, "not number!")
	except Exception as EOFError:
		pass

def passwordCommand(): # Command <password>
	global PASSWORT

	try:
		PASSWORT = str(getpass("Enter new PASSWORT: "))
	except Exception as TypeError:
		print(i, "not number!")
	except Exception as EOFError:
		pass


def interface():
	global THREAD_STATUS
	
	while True:
		try:
			command = str(input("Enter command: "))
		except Exception as EOFError:
			pass

		if command == 'exit':
			THREAD_STATUS = 0
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
		elif command == 'connections':
			if login() == 1234:
				printConnections()
		elif command == 'password':
			if login() == 1234:
				passwordCommand()
		elif command == 'send':
			if login() == 1234:
				sendCommand()
		elif command == 'buffer':
			if login() == 1234:
				bufferCommand()
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

	print()
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
