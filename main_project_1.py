from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui
from style import *

app=QApplication([])

win=QWidget()
win.resize(800,400)
win.setWindowTitle('Herbarium')
win.show()

win.setWindowIcon(QtGui.QIcon("icon.ico"))
win.setStyleSheet(styleproj)

label_p=QLabel('')
label_n=QLabel('Гербарій екзотичних квітів:')
label_per=QLabel('Перемикач картинок:')
label_n.setStyleSheet(styleproj)
label_per.setStyleSheet(styleproj)
btn_n=QPushButton("Наступна")
btn_l=QPushButton("Минула")
btn_l.setStyleSheet(styleproj)
btn_n.setStyleSheet(styleproj)
w1=QVBoxLayout()
w2=QVBoxLayout()
h1=QHBoxLayout()
h2=QHBoxLayout()
w1.addWidget(label_n)
w1.addWidget(label_p)
h2.addWidget(label_per)
h2.addWidget(btn_n)
h2.addWidget(btn_l)
w2.addLayout(h2)
h1.addLayout(w1)
h1.addLayout(w2)
win.setLayout(h1)
i=1
def change_plu():
    global i
    i=i+1
    pixmapimage=QPixmap(str(i)+"fl.jpg")
    pixmapimage=pixmapimage.scaled(400,400,Qt.KeepAspectRatio)
    label_p.setPixmap(pixmapimage)
    if i==5:
        i=0
btn_n.clicked.connect(change_plu)

def change_min():
    global i
    pixmapimage=QPixmap(str(i)+"fl.jpg")
    pixmapimage=pixmapimage.scaled(400,400,Qt.KeepAspectRatio)
    label_p.setPixmap(pixmapimage)
    if i==1:
        i=6
    i=i-1
btn_l.clicked.connect(change_min)

label_p.setFixedSize(400,400)
label_p.hide()
wpic,hpic=label_p.width(),label_p.height()
pixmapimage=QPixmap(str(i)+"fl.jpg")
pixmapimage=pixmapimage.scaled(wpic,hpic,Qt.KeepAspectRatio)
label_p.setPixmap(pixmapimage)


label_p.show()
app.exec()
