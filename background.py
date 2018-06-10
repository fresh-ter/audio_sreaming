# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
import sys
import random
import json




app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Hallo PyQt und Color")
window.resize(300 , 100)

# ni = 1

with open(r"c:\audio_streaming\color.txt", 'r', encoding='utf-8') as f:
    color_list = json.load(f)

# color_list = {1 : "#ff0000",
# 			  2 : "#008000",
# 			  3 : "#483d8b",
# 			  4 : "#6a5acd",
# 			  5 : "#800080",
# 			  6 : "#ffffff",
# 			  7 : "#ffff00",
# 			  8 : "#ff8c00",
# 			  9 : "#ff60cb"}

color_num = ('1','2','3','4','5','6','7','8','9')

pal = window.palette()
pal.setColor(QtGui.QPalette.Normal, QtGui.QPalette.Window,
			 QtGui.QColor(color_list.get(2)))
pal.setColor(QtGui.QPalette.Inactive, QtGui.QPalette.Window,
			 QtGui.QColor("#ff0000"))
window.setPalette(pal)

#a = 0



def tick():
	#print('tick')
	s = ''
	f = open(r"c:\audio_streaming\a.txt", "r", encoding="utf-8")
	for line in f:
		s += line

	if s == 'none':
		pal.setColor(QtGui.QPalette.Normal, QtGui.QPalette.Window,
			 	QtGui.QColor(color_list.get(random.randint(1,9))))
		window.setPalette(pal)
	elif s != 'none':
		for color in color_num:
			if s == color:
				pal.setColor(QtGui.QPalette.Normal, QtGui.QPalette.Window,
			 			QtGui.QColor(color_list.get(int(color))))
				window.setPalette(pal)

timer = QTimer()
timer.timeout.connect(tick)
timer.start(1000)


window.showFullScreen()

sys.exit(app.exec_())