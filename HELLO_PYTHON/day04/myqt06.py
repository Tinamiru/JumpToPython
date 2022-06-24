import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
import random

form_class = uic.loadUiType("myqt06.ui")[0]


class MainClass(QMainWindow, form_class):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        
        self.pb.clicked.connect(self.myclick)
        self.show()
        
    def myclick(self):
        arr = list(range(1, 45+1))
        random.shuffle(arr)
        
        self.lbl1.setText(str(arr[0]))
        self.lbl2.setText(str(arr[1]))
        self.lbl3.setText(str(arr[2]))
        self.lbl4.setText(str(arr[3]))
        self.lbl5.setText(str(arr[4]))
        self.lbl6.setText(str(arr[5]))
        

        
if __name__ == "__main__":
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()
