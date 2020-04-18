# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
import sys
import random
import json
from PyQt5.QtWidgets import QApplication, QWidget
from datetime import datetime



mainWindow = None

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        with open("color.txt", 'r', encoding='utf-8') as f:
            self.color_list = json.load(f)

        with open("number_color.txt", 'r', encoding='utf-8') as f:
            self.numberColor = json.load(f)

        self.pal = self.palette()
        self.time = 1

        self.to = 0

        self.timer = QTimer()
        self.c_s = -1

        self.initUI()


    def initUI(self):
        self.setWindowTitle("Hallo PyQt und Color")
        self.resize(300 , 100)

        print(self.pal)
        self.pal.setColor(QtGui.QPalette.Normal, QtGui.QPalette.Window,
                     QtGui.QColor(self.color_list.get('2')))
        self.pal.setColor(QtGui.QPalette.Inactive, QtGui.QPalette.Window,
                     QtGui.QColor("#ff0000"))
        self.setPalette(self.pal)

        self.show()

        self.timer.timeout.connect(self.tick)
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


    def tick(self):
        s = ''
        
        f = open("a.txt", "r", encoding="utf-8")
        for line in f:
            s += line

        if s == 'none':
            c = str(random.randint(1,int(self.numberColor)))

            while self.c_s == c:
                c = str(random.randint(1,int(self.numberColor)))

            self.c_s = c

            self.pal.setColor(QtGui.QPalette.Normal, QtGui.QPalette.Window,
                    QtGui.QColor(self.color_list.get(c)))
            self.setPalette(self.pal)
        elif s == 'exit':
            f = open("a.txt", "w", encoding="utf-8")
            f.write("none")
            f.close()
            sys.exit(app.exec_())
        elif s != 'none' and s != 'exit':
            for color in range(self.numberColor+1):
                if s == str(color):
                    self.pal.setColor(QtGui.QPalette.Normal, QtGui.QPalette.Window,
                            QtGui.QColor(self.color_list.get(str(color))))
                    self.setPalette(self.pal)


def main():
    global mainWindow

    app = QtWidgets.QApplication(sys.argv)

    mainWindow = MainWindow()
    mainWindow.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()