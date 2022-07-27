import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
import secrets
from day07.mymnist_gawi_load_class import HerKY

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
        
        hky = HerKY()
        
        me = self.le1.text()
        result = ""
        com = ""
        
        ans = -1
        if me == "가위":
            ans = hky.guess([[0, 0]])
        elif me == "바위":
            ans = hky.guess([[0, 0.5]])
        else:
            ans = hky.guess([[0, 1]])
            
        if ans == 0:
            com = "바위"
        elif ans == 1:
            com = "보"
        else: 
            com = "가위"
        
        if me == com:
            result = "비김"
        elif me == "가위" and com == "보" or me == "바위" and com == "가위" or me == "보" and com == "바위": 
            result = "이김"
        elif me != "가위" and me != "바위" and me != "보":
            result = "가위, 바위, 보만 입력해라."         
        else:
            result = "짐"
            
        self.le2.setText(com)            
        self.le3.setText(result)            

        
if __name__ == "__main__":
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()
