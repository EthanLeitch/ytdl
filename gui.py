import sys
import os, curses, sys, subprocess
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize    

encodingType = "MP4"

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)

        self.setMinimumSize(QSize(320, 140))    
        self.setWindowTitle("YouTube Downloader") 

        self.url = QLabel(self)
        self.url.setText('URL:')
        self.line = QLineEdit(self)

        self.line.move(80, 20)
        self.line.resize(200, 32)
        self.url.move(20, 20)

        radiobutton = QRadioButton("Download audio and video")
        radiobutton.setChecked(True)
        radiobutton.encoding = "MP4"
        radiobutton.toggled.connect(self.onClicked)
        layout.addWidget(radiobutton, 0, 0)

        radiobutton = QRadioButton("Only download audio")
        radiobutton.encoding = "MP3"
        radiobutton.toggled.connect(self.onClicked)
        layout.addWidget(radiobutton, 0, 1)

        pybutton = QPushButton('Download', self)
        pybutton.clicked.connect(self.clickMethod)
        pybutton.resize(200,32)
        pybutton.move(80, 100)        
    
    def onClicked(self):
        global encodingType
        radioButton = self.sender()
        if radioButton.isChecked():
            encodingType = radioButton.encoding
            print(encodingType)

    def clickMethod(self):
        global encodingType
        print(encodingType)

        if encodingType == "MP4":
            os.system("youtube-dl -f mp4 " + self.line.text())
        else:
            os.system("youtube-dl --extract-audio --audio-format mp3 "+ self.line.text())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet("QPushButton { color: white; background-color: green;} QPushButton:hover { background-color: teal; }")
    mainWin = Window()
    mainWin.show()
    sys.exit( app.exec_() )
