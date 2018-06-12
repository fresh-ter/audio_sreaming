# -*- coding: utf-8 -*-
import sys
import random
import socket
import time
from os import system
from sys import argv

NAME_CLIENT = "client main"
NUMBER_COMPUTER = None
DATE = None

n = 0
code = 0
exit = 0
passwort = "client"

IP = None    	############################################################################ /=)
PORT = 9090     ############################################################################ \=)

s = socket.socket()

print("NAME_CLIENT:" + NAME_CLIENT)

if len(argv) == 1:
	IP = str(input("Enter IP server`s: "))
	NUMBER_COMPUTER = int(input("Enter NUMBER_COMPUTER: "))
elif len(argv) > 1:
	print("-------------------------------------CMD-------------------------------------")
	print("Loading...")
	time.sleep(50)
	IP = str(argv[1])
	NUMBER_COMPUTER = int(argv[2])

f = open(r"c:\audio_streaming\number_computer.txt", "w", encoding="utf-8")
f.write(str(NUMBER_COMPUTER))
f.close()

f = open(r"c:\audio_streaming\date.txt", "r", encoding="utf-8")
DATE = str(f.read())
f.close()


def decode(msg):
	return msg.decode("utf-8")

def colorCommand(msg):
	print("Command <color>")
	if "start" in msg:
		print("Start color")
		system("start c:\\Python34\\python.exe c:\\audio_streaming\\background.py")
	elif "none" in msg:
		f = open(r"c:\audio_streaming\a.txt", "w", encoding="utf-8")
		f.write("none")
		f.close()
	elif "exit" in msg:
		print("Exit color")
		f = open(r"c:\audio_streaming\a.txt", "w", encoding="utf-8")
		f.write("exit")
		f.close()
	else:
		for c in ('1','2','3','4','5','6','7','8','9'):
			if c in msg:
				f = open(r"c:\audio_streaming\a.txt", "w", encoding="utf-8")
				f.write(c)
				f.close()
				break


def volumeCommand(msg):
	print("Command <volume>")

def testCommand():
	print("Command <test>")

def getsetCommand():
	print("Command <getset>")

	m = '3'
	m = m.encode("utf-8")

	s.send(m)
	
	address = s.recv(2048)
	address = decode(address)
	s.send(m)

	print("Address:", address)

	buffer_size = s.recv(2048)
	s.send(m)

	print("Buffer_size:", int(buffer_size.decode("utf-8")))

	str_code = s.recv(int(buffer_size.decode("utf-8")))

	f = open(address, 'w')
	f.write(str_code.decode("utf-8"))
	f.close()

def restartCommand():
	print("Command <restart>")

def exitCommand():
	pass




def commandMsg(msg):
	print("Msg:", msg)
	for d in ("color" , "volume" , "test", "getset"):
		if d in msg and d == "color":
			colorCommand(msg)
			return 3
		elif d in msg and d == "volume":
			volumeCommand(msg)
			return 3
		elif d in msg and d == 'test':
			testCommand()
			return 0
		elif d in msg and d == "getset":
			getsetCommand()
			return 3
		
	return 1
	



if len(argv) == 1:
	p = input("Passwort: ")
elif len(argv) > 1:
	p = passwort

print()
print()

if p == passwort:
	print("IP:", IP)
	print("PORT:", PORT)

	s.connect((IP , PORT))

	s.send(NAME_CLIENT.encode("utf-8"))
	print("NAME_CLIENT:", NAME_CLIENT)

	s.send(str(NUMBER_COMPUTER).encode("utf-8"))
	print("NUMBER_COMPUTER:", NUMBER_COMPUTER)

	print()

	m = s.recv(1024)
	print(decode(m))

	print()

	s.send(DATE.encode("utf-8"))
	print("DATE:", DATE)

	print()
	print()
	
	print("Connection successfully!")
	print()
	print("-------------------------------------")

	while True:
		data = s.recv(1024)

		if data:
			print("Data " + str(n) + " : " + decode(data))

			n += 1

			if decode(data) == 'exit':
				print("Command <exit>")

				#colorCommand("exit")

				codeStr = "3"
				s.send(codeStr.encode("utf-8"))
				break
			elif decode(data) == 'restart':
				print("Command <restart>")

				#colorCommand("exit")

				codeStr = "3"
				s.send(codeStr.encode("utf-8"))

				system("start c:\\Python34\\python.exe c:\\audio_streaming\\client_others.py" + ' ' + str(IP) + ' ' + str(NUMBER_COMPUTER))
				break

			code = commandMsg(decode(data))
			codeStr = str(code)
			s.send(codeStr.encode("utf-8"))
		print("-------------------------------------")

	s.close()

