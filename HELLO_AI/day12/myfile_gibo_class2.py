import numpy as np


class RaoGibo:

    def __init__(self):
        self.flagWb = True
        self.arr2D = np.zeros((20, 20), dtype="int")
        self.givo2db()
        
    def getGibo(self):
        file_name = "0_0_1_2.psq"
        arr_i = []
        arr_j = []
        f = open(file_name, 'r')
        lines = f.readlines()
        for line in lines:
            arr_split = line.split(",")
            mylen = len(arr_split)
            if mylen == 3:
                try:
                    i = int(arr_split[0]) - 1
                    j = int(arr_split[1]) - 1
                    arr_i.append(i)
                    arr_j.append(j)
                except:
                    pass
        f.close()
        return arr_i, arr_j

    def oneline(self, arr2D):
        mystr = ""
        for i in arr2D:
            for j in i:
               mystr += str(j)
        return mystr
    
    def givo2db(self):
        arr_i, arr_j = self.getGibo()
        for i in range(len(arr_i)):
            ii = arr_i[i]
            jj = arr_j[i]
            if self.flagWb:
                self.arr2D[ii][jj] = 1
            else:
                self.arr2D[ii][jj] = 2
            str = self.oneline(self.arr2D)
            print(i, ii, jj, str)
            self.flagWb = not self.flagWb
    
        print(arr_i)
        print(arr_j)

        
if __name__ == '__main__':
    rg = RaoGibo()
    
