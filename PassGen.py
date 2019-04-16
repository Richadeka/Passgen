from PyQt5.QtWidgets import QLabel, QCheckBox, QPushButton, QVBoxLayout, QApplication, QWidget
import sys
from PyQt5 import *
from PyQt5.QtCore import *
import random
import random

icon='img/password.png'
alpha=['q','w','e','r','t','y','u','i','o','p','l','k','j','h','g','f','d','s','a','z','x','c','v','b','n','m','M','N','B','V','C','X','Z','A','S','D','F','G','H','J','K','L','P','O','I','U','Y','T','R','E','W','Q']
sc=['!','@','#','$','%','&','*']
num=['1','2','3','4','5','6','7','8','9','0']

def createpass(a,b):
    z=[]
    if a==1:
        pl=alpha+sc+num
        for i in range (b):
            n=random.choice(pl)
            z.append(n)
    elif a==2:
        pl=alpha+num
        for i in range (b):
            n=random.choice(pl)
            z.append(n)
    elif a==3:
        pl=alpha+sc
        for i in range (b):
            n=random.choice(pl)
            z.append(n)
    elif a==4:
        pl=alpha
        for i in range (b):
            n=random.choice(pl)
            z.append(n)
    str= ''.join(z)
    return str





class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):



        self.setWindowTitle("Password Generator")
        self.setGeometry(540,150,400,500)
        self.setWindowIcon(QtGui.QIcon(icon))
        self.l1=QtWidgets.QLabel(self)
        self.l1.setText("<u>Password Generator V1.0</u>")
        self.l1.move(110,30)
        newfont = QtGui.QFont("Times", 12, QtGui.QFont.DemiBold)
        self.l1.setFont(newfont)

        self.l2=QtWidgets.QLineEdit(self)
        self.l2.setText("Password Here!")
        self.l2.setGeometry(0,0,350,50)
        self.l2.move(30,70)
        newfont1= QtGui.QFont("Times", 10)
        self.l2.setFont(newfont1)
        self.l2.setReadOnly(True)
        self.l2.setAlignment(Qt.AlignCenter);


        self.getp=QtWidgets.QPushButton(self)
        self.getp.setText("Generate Passoword")
        self.getp.setGeometry(QRect(0,0,140,40))
        self.getp.move(130,170)
        self.getp.setIcon(QtGui.QIcon("img/icon.png"))
        self.getp.setToolTip("Click this button to generate your Password")

        self.l3=QtWidgets.QLineEdit(self)
        self.l3.setText("0")
        self.l3.setGeometry(0,0,30,30)
        self.l3.move(100,230)
        self.l3.setAlignment(Qt.AlignCenter);

        self.l4=QtWidgets.QLabel(self)
        self.l4.setText("Enter no. of characters")
        self.l4.setGeometry(0,0,120,30)
        self.l4.move(150,230)
        self.l4.setAlignment(Qt.AlignCenter);

        self.l5=QtWidgets.QCheckBox("Include Numbers",self)
        self.l5.move(110,279)
        self.l5.setStyleSheet("QCheckBox{spacing:40px;}");


        self.l6=QtWidgets.QCheckBox("Include Special Characters",self)
        self.l6.move(110,309)
        self.l6.setStyleSheet("QCheckBox{spacing:20px;}");






        self.getp.clicked.connect(self.btn_click)






        self.show()

    def btn_click(self):
        if self.l3.text() == "0":
            self.l2.setText("Enter Atleast 1 Character!!!")
        else:
            if self.l5.isChecked()==True and self.l6.isChecked()==True:
                x=1;
            elif self.l5.isChecked()==True and self.l6.isChecked()==False:
                x=2
            elif self.l5.isChecked()==False and self.l6.isChecked()==True:
                x=3
            elif self.l5.isChecked()==False and self.l6.isChecked()==False:
                x=4
            y=int(self.l3.text())
            z=createpass(x,y)
            self.l2.setText(z)


app = QtWidgets.QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())
