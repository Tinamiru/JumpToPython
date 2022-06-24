import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.Qt import QButtonGroup

form_class = uic.loadUiType("myqt09.ui")[0]


class MainClass(QMainWindow, form_class):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

        
        self.pb0.clicked.connect(self.myclick)
        self.pb1.clicked.connect(self.myclick)
        self.pb2.clicked.connect(self.myclick)
        self.pb3.clicked.connect(self.myclick)
        self.pb4.clicked.connect(self.myclick)
        self.pb5.clicked.connect(self.myclick)
        self.pb6.clicked.connect(self.myclick)
        self.pb7.clicked.connect(self.myclick)
        self.pb8.clicked.connect(self.myclick)
        self.pb9.clicked.connect(self.myclick)
        
        self.pbcall.clicked.connect(self.mycall)
        self.pbdel.clicked.connect(self.mydel)
        
        self.show()
    def mydel(self):
        str = self.le.text()
        strDel = str[:-1]
        self.le.setText(strDel)
        
    def mycall(self):
        QMessageBox.information(self, "OK", self.le.text() + "로 전화를 겁니다.")
        
    def myclick(self):
        num = self.sender().text()
        
        self.le.insert(num)

      
if __name__ == "__main__":
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()
