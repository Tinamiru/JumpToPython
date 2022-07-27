import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
import secrets
from day06.mymnist_holl_load_class import HerKY


form_class = uic.loadUiType("myqt05.ui")[0]


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
        
        com = ""
        result = ""
        
        mine = self.le1.text()
        
        hky = HerKY()
        
        ans = -1
        if mine == "홀":
            ans = hky.guess([[1,0]])
        else:
            ans = hky.guess([[0,1]])
                       
        if ans == 0:
            com = "홀"
        else : 
            com = "짝"
        
        if mine == com :
            result = "이김"
        else :
            result = "짐"
        
        self.le2.setText(com)
        self.le3.setText(result)    
                
if __name__ == "__main__":
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()

