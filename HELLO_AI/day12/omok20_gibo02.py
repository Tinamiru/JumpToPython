import sys
from PyQt5 import uic, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox
import numpy as np
from day12.myfile_gibo_class import RaoGibo

form_class = uic.loadUiType("omok03.ui")[0]


class MainClass(QMainWindow, form_class): 

    def __init__(self):
        QMainWindow.__init__(self)
        
        self.arr_i = [0, 0, 0, 0, 0]
        self.arr_j = [0, 1, 2, 3, 4]

        rg = RaoGibo()
        self.arr_i, self.arr_j = rg.getGibo("0_0_1_2.psq")
        
        self.idx_g = 0
        self.flagWb = False
        self.flagIng = True
        self.arr2D = np.zeros((20, 20))
        self.pb2D = []
        self.setupUi(self)
        
        for i in range(20): 
            line = []
            for j in range(20):
                btn = QPushButton('', self)
                btn.setIcon(QtGui.QIcon("0.png"))
                btn.setGeometry((j * 40) + 40, (i * 40) + 60, 40, 40)
                btn.setIconSize(QtCore.QSize(40, 40))
                btn.setToolTip("{},{}".format(i, j))
                btn.clicked.connect(self.myclick)
                line.append(btn)
            self.pb2D.append(line)
            
        self.myrender()        
        self.pb.clicked.connect(self.mygibo)

        self.show()
    
    def myclick(self):
        idx = self.sender().toolTip().split(",")
        i = int(idx[0])
        j = int(idx[1])
        stone = -1
        if self.flagWb:
            self.arr2D[i][j] = 1
            stone = 1
        else:
            self.arr2D[i][j] = 2
            stone = 2
            
        up = self.checkUP(i, j, stone)
        dw = self.checkDown(i, j, stone)
        ri = self.checkRi(i, j, stone)
        le = self.checkLe(i, j, stone)
        ur = self.checkUr(i, j, stone)
        dl = self.checkDl(i, j, stone)
        ul = self.checkUl(i, j, stone)
        dr = self.checkDr(i, j, stone)
        
        d1 = up + dw + 1
        d2 = ri + le + 1
        d3 = ur + dl + 1
        d4 = ul + dr + 1
    
        self.myrender()
        if (d1 == 5 or d2 == 5 or d3 == 5 or d4 == 5):
            if self.flagWb:
                win = "백돌"
                QMessageBox.information(self, "확인", win + "이 이겼습니다.")
                self.flagIng = False
            else:
                win = "흑돌"
                QMessageBox.information(self, "확인", win + "이 이겼습니다.")
                self.flagIng = False
        
        self.flagWb = not self.flagWb
        
    def checkUP(self, i, j, stone):
        cnt = 0
        try:
            while True:
                i -= 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt

    def checkDown(self, i, j, stone):
        cnt = 0
        try:
            while True:
                i += 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt

    def checkRi(self, i, j, stone):
        cnt = 0
        try:
            while True:
                j += 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt

    def checkLe(self, i, j, stone):
        cnt = 0
        try:
            while True:
                j -= 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt

    def checkUr(self, i, j, stone):
        cnt = 0
        try:
            while True:
                i -= 1
                j += 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt

    def checkUl(self, i, j, stone):
        cnt = 0
        try:
            while True:
                i -= 1
                j -= 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt

    def checkDr(self, i, j, stone):
        cnt = 0
        try:
            while True:
                i += 1
                j += 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt

    def checkDl(self, i, j, stone):
        cnt = 0
        try:
            while True:
                i += 1
                j -= 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
    
    def mygibo(self):
        if not self.flagIng:
            return
        
        i = self.arr_i[self.idx_g]    
        j = self.arr_j[self.idx_g]
        
        stone = -1
        if self.flagWb:
            self.arr2D[i][j] = 1
            stone = 1
        else: 
            self.arr2D[i][j] = 2
            stone = 2
            
        self.idx_g += 1
        
        up = self.checkUP(i, j, stone)
        dw = self.checkDown(i, j, stone)
        ri = self.checkRi(i, j, stone)
        le = self.checkLe(i, j, stone)
        ur = self.checkUr(i, j, stone)
        dl = self.checkDl(i, j, stone)
        ul = self.checkUl(i, j, stone)
        dr = self.checkDr(i, j, stone)
        
        d1 = up + dw + 1
        d2 = ri + le + 1
        d3 = ur + dl + 1
        d4 = ul + dr + 1
        
        self.myrender()
        if (d1 == 5 or d2 == 5 or d3 == 5 or d4 == 5):
            if self.flagWb:
                win = "백돌"
                QMessageBox.information(self, "확인", win + "이 이겼습니다.")
                self.flagIng = False
            else:
                win = "흑돌"
                QMessageBox.information(self, "확인", win + "이 이겼습니다.")
                self.flagIng = False
                
        self.flagWb = not self.flagWb    
            
    def myrender(self):
        for i in range(20):
            for j in range(20):
                if self.arr2D[i][j] == 0:
                    self.pb2D[i][j].setIcon(QtGui.QIcon("0.png"))
                if self.arr2D[i][j] == 1:
                    self.pb2D[i][j].setIcon(QtGui.QIcon("1.png"))
                if self.arr2D[i][j] == 2:
                    self.pb2D[i][j].setIcon(QtGui.QIcon("2.png"))
    
    def reset(self):
        for i in range(20):
            for j in range(20):
                self.arr2D[i][j] = 0
        self.myrender()
        self.flagIng = True
        self.flagWb = False
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()
