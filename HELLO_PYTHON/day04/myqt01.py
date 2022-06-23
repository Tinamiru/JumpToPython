import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic

form_class = uic.loadUiType("myqt01.ui")[0]


class MorningToEvening(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.goodEvening)
        self.initUI() 
    
    def initUI(self):
        self.setWindowTitle('Morning To Evening') # 윈도우창의 제목생성 메서드
        self.resize(400, 300)
    
    def goodEvening(self):
        self.lbl.setText("good Evening")
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MorningToEvening()
    myWindow.show()
    app.exec_()