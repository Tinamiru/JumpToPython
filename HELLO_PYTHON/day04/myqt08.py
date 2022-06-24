import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

form_class = uic.loadUiType("myqt08.ui")[0]

class MainClass(QMainWindow, form_class):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        
        self.pb.clicked.connect(self.myclick)
        self.show()
        
    def myclick(self):
        self.te.clear()
        
        a = int(self.le1.text())
        b = int(self.le2.text())
        arr= range(a,b+1)
        
        for i in arr:
            star = ""
            for j in range(i):
                star += "*"
            self.te.append(star)
        
if __name__ == "__main__":
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()
