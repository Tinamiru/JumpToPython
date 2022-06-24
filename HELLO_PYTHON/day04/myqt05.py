import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
import secrets

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
        
        me = self.le1.text()
        com = str(self.comChoise())
        self.le2.setText(com)
        
        if me == com :
            self.le3.setText("이김")
        else :
            self.le3.setText("짐")            
        
        
        
    def comChoise(self):
        arr = ["홀", "짝"]
        return secrets.choice(arr)
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()
