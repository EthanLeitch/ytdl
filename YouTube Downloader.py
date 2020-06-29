from __future__ import unicode_literals
import os, curses, sys, subprocess, youtube_dl, getpass
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import *
from PyQt5.QtCore import QSize    
import time


encodingType = "MP4"
pybutton = ""
urlEmpty = ""
invalid = ""
progress = ""
finishedDownloading = ""
p = ""
dropdown = ""

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)

        self.setFixedSize(360, 140)
        self.setWindowTitle("YouTube Downloader") 
        self.setWindowIcon(QIcon('/home/' + getpass.getuser() + '/ytdl/icon.png'))

        self.url = QLabel(self)
        self.url.setText('URL:')

        self.line = QLineEdit(self)
        self.line.move(80, 20)
        self.line.resize(200, 32)
        
        self.url.move(20, 20)

        output = QLabel(self)
        output.setText("Output Format:")
        output.move(80, 60)

        global dropdown

        dropdown = QComboBox(self)
        dropdown.addItem("MP4")
        dropdown.addItem("MP3")
        dropdown.move(180, 60)

        dropdown.activated[str].connect(self.outputFormat)

        #radiobutton = QRadioButton("Download audio and video")
        #radiobutton.setChecked(True)
        #radiobutton.encoding = "MP4"
        #radiobutton.toggled.connect(self.onClicked)
        #layout.addWidget(radiobutton, 0, 0)

        #radiobutton = QRadioButton("Only download audio")
        #radiobutton.encoding = "MP3"
        #radiobutton.toggled.connect(self.onClicked)
        #layout.addWidget(radiobutton, 0, 1)

        global pybutton

        pybutton = QPushButton('Download', self)
        pybutton.clicked.connect(self.clickMethod)
        pybutton.resize(200,32)
        pybutton.move(80, 100)    

        global urlEmpty

        urlEmpty = QLabel(self)
        urlEmpty.setText('Url is empty.')
        urlEmpty.setStyleSheet("color: red")
        urlEmpty.resize(200, 32)
        urlEmpty.move(5, 100)
        urlEmpty.hide()

        global invalid

        invalid = QLabel(self)
        invalid.setText('Invalid url.')
        invalid.setStyleSheet("color: red")
        invalid.resize(200, 32)
        invalid.move(5, 100)
        invalid.hide()

        global progress

        progress = QProgressBar(self)
        progress.setGeometry(80, 105, 200, 25)
        progress.hide()

        global finishedDownloading

        finishedDownloading = QLabel(self)
        finishedDownloading.setText('Saved to Downloads!')
        finishedDownloading.setGeometry(80, 105, 200, 80)
        finishedDownloading.hide()
    
    def onClicked(self):
        global encodingType
        radioButton = self.sender()
        if radioButton.isChecked():
            encodingType = radioButton.encoding
            print(encodingType)

    def outputFormat(self, text):
        global encodingType
        if text == "MP3":
            print("mp3")
            encodingType = "MP3"
        if text == "MP4":
            print("mp4")
            encodingType = "MP4"

    def clickMethod(self):
        global encodingType
        global pybutton
        global finishedDownloading
        print(encodingType)
        
        if self.line.text() == "":
            urlEmpty.show()
            invalid.hide()
        else:
            if "https://www.youtube.com/watch?v=" not in self.line.text() and self.line.text() != "":
                invalid.show()
                urlEmpty.hide()
            else:
                pybutton.hide()
                urlEmpty.hide()
                invalid.hide()
                progress.show()
                finishedDownloading.hide()

                if encodingType == "MP4":
                    ytdl_opts = {
                        'format': 'bestvideo[ext=m4a]+bestaudio/best',
                        'extract-audio': 'True',
                        'progress_hooks': [self.my_hook],
                        'outtmpl': '/home/' + getpass.getuser() + '/Downloads/%(title)s.%(ext)s',}
                if encodingType == "MP3":
                    ytdl_opts = {
                        'format': 'bestaudio/best',
                        'postprocessors': [{
                            'key': 'FFmpegExtractAudio',
                            'preferredcodec': 'mp3',
                            'preferredquality': '192',
                        }],
     
                        'outtmpl': '/home/' + getpass.getuser() + '/Downloads/%(title)s.%(ext)s',        
                        'noplaylist' : True,        
                        'progress_hooks': [self.my_hook],
                    }
                with youtube_dl.YoutubeDL(ytdl_opts) as ydl:
                    print(self.line.text())
                    ydl.download([self.line.text()])
                    #self.setMinimumSize(QSize(320, 170))
                    #while True:
                    #    line = p
                    #    string = str(line)
                    #    urlfinishedDownloading = self.line.text().replace("https://www.youtube.com/watch?v=", "")
                    #    print(urlfinishedDownloading)
                    #    a = string.replace("b'[youtube] ", "")
                    #    b = a.replace("b''", "")
                    #    c = b.replace("b'[download] ", "")
                    #    d = c.replace(urlfinishedDownloading + ": ", "")
                    #    print(d)
                    #    finishedDownloading.show()
                    #    finishedDownloading.setText(d)
                    #    if not line: break
                    #    progress.setValue(100)
                #else:
                #    os.system("youtube-dl --extract-audio --audio-format mp3 "+ self.line.text())
                #    progress.setValue(100)

    def my_hook(self, d):
        global finishedDownloading
        global pybutton
        if d['status'] == 'finished':
            file_tuple = os.path.split(os.path.abspath(d['filename']))
            print("Done downloading {}".format(file_tuple[1]))
            progress.hide()
            self.setFixedSize(360, 160)
            finishedDownloading.show()
            pybutton.show()
        if d['status'] == 'downloading':
            p = d['_percent_str']
            p = p.replace('%','')
            progress.setValue(float(p))
            print(d['filename'], d['_percent_str'], d['_eta_str'])

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet("QPushButton { color: white; background-color: green;} QPushButton:hover { background-color: teal; }")
    mainWin = Window()
    mainWin.show()
    sys.exit( app.exec_() )