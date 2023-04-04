import sys
from PyQt5 import QtWidgets
import random

player = "x"
computer = "o"
field = []
rand = 0
app = QtWidgets.QApplication(sys.argv)
win = QtWidgets.QMainWindow()
win.setGeometry(1200, 300, 375, 420)
win.setWindowTitle("Tic Tac Toe")
btn1 = QtWidgets.QPushButton(win)
btn2 = QtWidgets.QPushButton(win)
btn3 = QtWidgets.QPushButton(win)
btn4 = QtWidgets.QPushButton(win)
btn5 = QtWidgets.QPushButton(win)
btn6 = QtWidgets.QPushButton(win)
btn7 = QtWidgets.QPushButton(win)
btn8 = QtWidgets.QPushButton(win)
btn9 = QtWidgets.QPushButton(win)

def restart():
    global field
    field = []
def switch():
    global player
    global computer
    if player=="x":
        player="o"
        computer="x"
    else:
        player = "x"
        computer="o"

def ai():
    global field
    if computer=="o" and field==[]:
        return
    global rand
    counter = 0
    while True:
        if counter>1000:
            break
        counter+=1
        rand=random.randint(1,9)
        if rand in field:
            continue
        else:
            field.append(rand)
            if rand==1:
                btn1.setText(computer)
            elif rand==2:
                btn2.setText(computer)
            elif rand==3:
                btn3.setText(computer)
            elif rand==4:
                btn4.setText(computer)
            elif rand==5:
                btn5.setText(computer)
            elif rand==6:
                btn6.setText(computer)
            elif rand==7:
                btn7.setText(computer)
            elif rand==8:
                btn8.setText(computer)
            elif rand==9:
                btn9.setText(computer)
            break

def window():


    btn1.setGeometry(50,50,75,75)
    btn1.clicked.connect(lambda: btn1.setText(player))
    btn1.clicked.connect(lambda: field.append(1))
    btn1.clicked.connect(ai)


    btn2.setGeometry(150,50,75,75)
    btn2.clicked.connect(lambda: btn2.setText(player))
    btn2.clicked.connect(lambda: field.append(2))
    btn2.clicked.connect(ai)



    btn3.setGeometry(250,50,75,75)
    btn3.clicked.connect(lambda: btn3.setText(player))
    btn3.clicked.connect(lambda: field.append(3))
    btn3.clicked.connect(ai)



    btn4.setGeometry(50,150,75,75)
    btn4.clicked.connect(lambda: btn4.setText(player))
    btn4.clicked.connect(lambda: field.append(4))
    btn4.clicked.connect(ai)



    btn5.setGeometry(150,150,75,75)
    btn5.clicked.connect(lambda: btn5.setText(player))
    btn5.clicked.connect(lambda: field.append(5))
    btn5.clicked.connect(ai)



    btn6.setGeometry(250,150,75,75)
    btn6.clicked.connect(lambda: btn6.setText(player))
    btn6.clicked.connect(lambda: field.append(6))
    btn6.clicked.connect(ai)



    btn7.setGeometry(50,250,75,75)
    btn7.clicked.connect(lambda: btn7.setText(player))
    btn7.clicked.connect(lambda: field.append(7))
    btn7.clicked.connect(ai)



    btn8.setGeometry(150,250,75,75)
    btn8.clicked.connect(lambda: btn8.setText(player))
    btn8.clicked.connect(lambda: field.append(8))
    btn8.clicked.connect(ai)



    btn9.setGeometry(250,250,75,75)
    btn9.clicked.connect(lambda: btn9.setText(player))
    btn9.clicked.connect(lambda: field.append(9))
    btn9.clicked.connect(ai)



    btnR = QtWidgets.QPushButton(win)
    btnR.setText("Restart!")
    btnR.setGeometry(157,350,60,30)
    btnR.clicked.connect(restart)
    btnR.clicked.connect(lambda: btn1.setText(" "))
    btnR.clicked.connect(lambda: btn2.setText(" "))
    btnR.clicked.connect(lambda: btn3.setText(" "))
    btnR.clicked.connect(lambda: btn4.setText(" "))
    btnR.clicked.connect(lambda: btn5.setText(" "))
    btnR.clicked.connect(lambda: btn6.setText(" "))
    btnR.clicked.connect(lambda: btn7.setText(" "))
    btnR.clicked.connect(lambda: btn8.setText(" "))
    btnR.clicked.connect(lambda: btn9.setText(" "))
    btnR.clicked.connect(ai)

    btnS = QtWidgets.QPushButton(win)
    btnS.setText("Play as: o")
    btnS.setGeometry(257,350,60,30)
    btnS.clicked.connect(lambda: btnS.setText("Play as: " + player))
    btnS.clicked.connect(switch)
    btnS.clicked.connect(restart)
    btnS.clicked.connect(lambda: btn1.setText(" "))
    btnS.clicked.connect(lambda: btn2.setText(" "))
    btnS.clicked.connect(lambda: btn3.setText(" "))
    btnS.clicked.connect(lambda: btn4.setText(" "))
    btnS.clicked.connect(lambda: btn5.setText(" "))
    btnS.clicked.connect(lambda: btn6.setText(" "))
    btnS.clicked.connect(lambda: btn7.setText(" "))
    btnS.clicked.connect(lambda: btn8.setText(" "))
    btnS.clicked.connect(lambda: btn9.setText(" "))
    btnS.clicked.connect(ai)




    win.show()
    sys.exit(app.exec_())

window()