# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
import sys
import random
import json
from PyQt5.QtWidgets import QApplication, QWidget
from datetime import datetime


app = QtWidgets.QApplication(sys.argv)
ex = None

class Example(QWidget):
    #pal  = None
    def __init__(self):
        super().__init__()

        self.pal = self.palette()
        self.time = 1

        self.to = 0

        self.timer = QTimer()
        self.c_s = "#6a5acd"

        self.initUI()
        


    def initUI(self):
        self.setWindowTitle("Hallo PyQt und Color")
        self.resize(300 , 100)

        print(self.pal)
        self.pal.setColor(QtGui.QPalette.Normal, QtGui.QPalette.Window,
                     QtGui.QColor(color_list.get('2')))
        self.pal.setColor(QtGui.QPalette.Inactive, QtGui.QPalette.Window,
                     QtGui.QColor("#ff0000"))
        self.setPalette(self.pal)

        

        self.show()

        self.timer.timeout.connect(tick)
        self.timer.start(self.time*1000)

    def keyPressEvent(self, e):
        print(123)
        d = datetime.now()
        d_s = d.second + d.microsecond/1000000

        self.time = d_s - self.to
        self.to = d_s
        print("time " + str(self.time))
        print("to " + str(self.to))

        #self.timer.cancel()
        #self.timer.timeout.connect(tick)
        self.timer.setInterval(self.time*1000)

        
        print()
        # if e.key() == Qt.Key_Escape:
        #     self.close()


# window = QtWidgets.QWidget()
# window.
# window.

# r"c:\audio_streaming\color.txt"
with open("color.txt", 'r', encoding='utf-8') as f:
    color_list = json.load(f)

# r"c:\audio_streaming\number_color.txt"
with open("number_color.txt", 'r', encoding='utf-8') as f:
    numberColor = json.load(f)

# pal = window.palette()
# pal.setColor(QtGui.QPalette.Normal, QtGui.QPalette.Window,
#            QtGui.QColor(color_list.get('2')))
# pal.setColor(QtGui.QPalette.Inactive, QtGui.QPalette.Window,
#            QtGui.QColor("#ff0000"))
# window.setPalette(pal)

def pressKey():
    print("Hello!")


def tick():
    s = ''
    
    f = open("a.txt", "r", encoding="utf-8")
    for line in f:
        s += line

    if s == 'none':
        c = str(random.randint(1,int(numberColor)))

        if (c == ex.c_s) and (c != "#800080"):
            c = "#800080"
        elif (c == ex.c_s) and (c == "#800080"):
            c = "#6a5acd"

        ex.c_s = c

        ex.pal.setColor(QtGui.QPalette.Normal, QtGui.QPalette.Window,
                QtGui.QColor(color_list.get(c)))
        ex.setPalette(ex.pal)
    elif s == 'exit':
        f = open("a.txt", "w", encoding="utf-8")
        f.write("none")
        f.close()
        sys.exit(app.exec_())
    elif s != 'none' and s != 'exit':
        for color in range(numberColor+1):
            if s == str(color):
                ex.pal.setColor(QtGui.QPalette.Normal, QtGui.QPalette.Window,
                        QtGui.QColor(color_list.get(str(color))))
                ex.setPalette(ex.pal)

# timer = QTimer()
# timer.timeout.connect(tick)
# timer.start(ex.time*1000)

#window.keyPressEvent.connect(pressKey)

ex = Example()

# timer = QTimer()
# timer.timeout.connect(tick)
# timer.start(ex.time*1000)


ex.show()

sys.exit(app.exec_())