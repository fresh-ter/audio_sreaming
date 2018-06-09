# -*- coding: utf-8 -*-
import sys
import random
import socket

color_list = {1 : "#ff0000",
			  2 : "#008000",
			  3 : "#483d8b",
			  4 : "#6a5acd",
			  5 : "#800080",
			  6 : "#ffffff",
			  7 : "#ffff00",
			  8 : "#ff8c00",
			  9 : "#ff60cb"}

n = 0
code = 0
exit = 0
passwort = "client"

ip = '127.0.0.1' ############################################################################ /=)
port = 9090      ############################################################################ \=)

ip = str(input("Enter IP server`s: "))


def decode(msg):
	return msg.decode("utf-8")


def interpret(msg):
	for d in ("color" , "volume"):
		if d in msg and d == "color":
			color_disp(msg)
			return 0
		elif d in msg and d == "volume":
			volume_sys(msg)
			return 0
		elif msg == "exit":
			exit = 1
			return 0
	return 1


def color_disp(msg):
	print("color_disp")
	if "start" in msg:
		print("Start color")
		#=============================================== CMD =====================================
	elif "none" in msg:
		f = open(r"c:\audio_streaming\a.txt", "w", encoding="utf-8")
		f.write("none")
		f.close()
	else:
		for c in ('1','2','3','4','5','6','7','8','9'):
			if c in msg:
				f = open(r"c:\audio_streaming\a.txt", "w", encoding="utf-8")
				f.write(c)
				f.close()
				break


def volume_sys(msg):
	print("volume_sys")





p = input("Passwort: ")

if p == passwort:
	
	sock = socket.socket()
	sock.connect((ip , port))
	
	print("Hello world!")

	while True:
		data = sock.recv(1024)

		if data:
			print("Data " + str(n) + " : " + decode(data))

			n += 1

			if decode(data) == 'exit':
				print(4321)
				break
			code = interpret(decode(data))
			ucode = str(code)
			sock.send(ucode.encode("utf-8"))
		print(1234)

	sock.close()

sys.exit(app.exec_())