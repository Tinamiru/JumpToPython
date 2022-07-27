import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
import secrets
from day08.mymnist_hit_load_class import HerKY

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
        result = "1~9만 쓰라"
        
        mine = int(self.le1.text())
        
        hky = HerKY()
        
        if mine < 9+1 :
            if mine > 0 :
                mineArray = [0, 0, 0, 0, 0, 0, 0, 0, 0]
                mineArray[mine - 1] += 1
                com = hky.guess([mineArray]) + 1
                if mine == com:
                    result = "이김"
                else:
                    result = "짐"
                
        
        self.le2.setText(str(com))
        self.le3.setText(result)    

                
if __name__ == "__main__":
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()

