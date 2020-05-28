from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5 import QtWidgets

app = QApplication([])

label = QLabel('Enter a YouTube URL in the box below')
label.show()

urlbox = QtWidgets.QLineEdit()
urlbox.show()
app.exec_()