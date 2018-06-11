# -*- coding: utf-8 -*-
import sys
import random
import socket
from os import system

n = 0
code = 0
exit = 0
passwort = "client"

IP = None    	############################################################################ /=)
PORT = 9090     ############################################################################ \=)

IP = str(input("Enter IP server`s: "))


def decode(msg):
	return msg.decode("utf-8")

def colorCommand(msg):
	print("color_disp")
	if "start" in msg:
		print("Start color")
		system("c:\\Python34\\python.exe c:\\audio_streaming\\background.py")
	elif "none" in msg:
		f = open(r"c:\audio_streaming\a.txt", "w", encoding="utf-8")
		f.write("none")
		f.close()
	elif "exit" in msg:
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
	print("volume_sys")

def testCommand():
	print("test")


def commandMsg(msg):
	for d in ("color" , "volume" , "test"):
		if d in msg and d == "color":
			colorCommand(msg)
			return 3
		elif d in msg and d == "volume":
			volumeCommand(msg)
			return 3
		elif d in msg and d == 'test':
			testCommand()
			return 0
		
	return 1
	




p = input("Passwort: ")

if p == passwort:
	
	s = socket.socket()
	s.connect((IP , PORT))
	
	print("Hello world!")

	while True:
		data = s.recv(1024)

		if data:
			print("Data " + str(n) + " : " + decode(data))

			n += 1

			if decode(data) == 'exit':
				print("exit")

				colorCommand("exit")

				codeStr = "3"
				s.send(codeStr.encode("utf-8"))
				break

			code = commandMsg(decode(data))
			codeStr = str(code)
			s.send(codeStr.encode("utf-8"))
		print("-------------------------------------")

	s.close()

