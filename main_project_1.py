from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui

app=QApplication([])

win=QWidget()
win.resize(800,400)
win.setWindowTitle('Herbarium')
win.show()

label_p=QLabel('')
label_p.setFixedSize(400,400)
label_n=QLabel('Гербарій екзотичних квітів:')
label_per=QLabel('Перемикач картинок:')
label_p.hide()
pixmapimage=QPixmap("1fl.jpg")
wpic,hpic=label_p.width(),label_p.height()
pixmapimage=pixmapimage.scaled(400,400,Qt.KeepAspectRatio)
label_p.setPixmap(pixmapimage)
label_p.show()

btn_n=QPushButton("Наступна")
btn_l=QPushButton("Минула")

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
def change():
    global i
    
    pixmapimage=QPixmap(str(i)+"fl.jpg")
    label_p.setPixmap(pixmapimage)
    pixmapimage=pixmapimage.scaled(400,400,Qt.KeepAspectRatio)
    if i==6:
        i=0
    i=i+1
btn_n.clicked.connect(change)

app.exec()
