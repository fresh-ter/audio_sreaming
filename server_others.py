# -*- coding: utf-8 -*-
from getpass import getpass
import socket

SOCKET = socket.socket()

PASSWORT = "hackers"
IP = None
PORT = None
LISTEN = None
CONNECTS = 0

#			   ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",]
#   computer    1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19
connect_list = []
address_list = []

index = 0

def printInfo():
	print()
	print("________INFO________")
	print("IP sever`s:"  +IP)
	print("PORT sever`s:" + PORT)
	print("LISTEN sever`s:" + LISTEN)
	print("PASSWORT sever`s:" + PASSWORT)
	print("CONNECTS sever`s:" + CONNECTS)
	print()


def login():
	i = 0

	while i < 4:
		p = str(getpass("password: "))

		if p == PASSWORD:	
			return 1234
		print("Incorrect password.")
		i =+ 1

	print("Authorization completed unsuccessfully!")
	#exit()


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

def interface():
	while True:
		command = input("Enter command: ")

		if command:
			if command == 'exit':
				break
			elif command == 'connect':
				p = input("Passwort: ")
				if p == passwort:
					i = input("Enter number connected   (int <= 19)  : ")
					connected(int(i))
			elif command == 'send':
				p = input("Passwort: ")
				if p == passwort:
					data_get = computer()
					if data_get != "qwerty":
						ret(data_get.decode("utf-8"))
			else:
				print("Wir weisen diese <Command> nicht!")
			print()
		elif not command:
			print("You not enter command!")
			continue
		else:
			print("Error!")
			continue

def createSocket():
	print()
	
	IP = str(input("IP: "))
	PORT = int(input("PORT: "))
	LISTEN = int(input("LISTEN: "))

	print("Creating Socket...")

	SOCKET.bind((IP , PORT))
	SOCKET.listen(LISTEN)

	print("Socket created successfully!")
	print()

def destroySocket():
	SOCKET.close()

def main():
	createSocket()
	printInfo()

if __name__ == '__main__':
	main()

print("Auf fiedersehen!")
