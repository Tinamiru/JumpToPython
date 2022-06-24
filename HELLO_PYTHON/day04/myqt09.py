import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

form_class = uic.loadUiType("myqt08.ui")[0]

class MainClass(QMainWindow, form_class):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        
        self.pb0.clicked.connect(self.myclick(0))
        self.pb1.clicked.connect(self.myclick(1))
        self.pb2.clicked.connect(self.myclick(2))
        self.pb3.clicked.connect(self.myclick(3))
        self.pb4.clicked.connect(self.myclick(4))
        self.pb5.clicked.connect(self.myclick(5))
        self.pb6.clicked.connect(self.myclick(6))
        self.pb7.clicked.connect(self.myclick(7))
        self.pb8.clicked.connect(self.myclick(8))
        self.pb9.clicked.connect(self.myclick(9))
        
        self.show()
        
    def myclick(self, btnNum):
        self.le.append(str(btnNum))
        
if __name__ == "__main__":
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()
