import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

form_class = uic.loadUiType("myqt0a.ui")[0]

class MainClass(QMainWindow, form_class):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        
        self.pb.clicked.connect(self.myclick)
        self.le3.returnPressed.connect(self.myclick)
        self.show()
        
    def myclick(self):
        self.le4.clear()
        
        a = int(self.le1.text())
        b = int(self.le2.text())
        powNum = int(self.le3.text())
        sum = 0
        
        for i in range(a,b+1):
            if i % powNum == 0:
                sum += i
        self.le4.setText(str(sum))
        
if __name__ == "__main__":
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()
