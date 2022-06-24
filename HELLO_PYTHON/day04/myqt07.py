import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
import secrets

form_class = uic.loadUiType("myqt07.ui")[0]


class MainClass(QMainWindow, form_class):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.le1.returnPressed.connect(self.myclick)
        self.pb.clicked.connect(self.myclick)
        self.show()
        
    def myclick(self):
        self.le2.clear()
        self.le3.clear()
        
        me = self.le1.text()
        com = str(self.comChoise())
        self.le2.setText(com)
        
        if me == com :
            self.le3.setText("비김")
        elif me == "가위" and com == "보" or me == "바위" and com == "가위" or me == "보" and com == "바위": 
            self.le3.setText("이김")
        elif me != "가위" and me != "바위" and me != "보":
            self.le3.setText("가위, 바위, 보만 입력해라.")            
        else :
            self.le3.setText("짐")            
        
        
        
    def comChoise(self):
        arr = ["가위", "바위", "보"]
        return secrets.choice(arr)
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()
