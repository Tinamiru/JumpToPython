import numpy as np

class RaoGibo:
    def __init__(self):
        self.gibo = []
        self.gibo_ai = []
        self.ans = []
        self.win = -1

        
        self.flagWb = True
        self.arr2D = np.zeros((20,20),dtype="int")
        
        self.gibo.append(self.oneline(self.arr2D)[0:40])
        self.gibo_ai.append(self.oneline_ai(self.arr2D)[0:40])

        self.gibo2db()
        self.insert_db()
        
    def insert_db(self):
        
        for i in range(len(self.ans)):
            print(self.gibo[i],self.gibo_ai[i],self.ans[i],self.win)
        

    def getGibo(self):
        file_name = "0_0_1_2.psq"
        arr_i =[]
        arr_j =[]
        f = open(file_name, 'r')
        lines = f.readlines()
        for line in lines:
            arr_split = line.split(",")
            mylen = len(arr_split)
            if mylen == 3:
                try:
                    i = int(arr_split[0])-1
                    j = int(arr_split[1])-1
                    arr_i.append(i)
                    arr_j.append(j)
                except:
                    pass
        f.close()
        return arr_i,arr_j
    
    def oneline(self,arr2D):
        mystr = ""
        for i in arr2D:
            for j in i:
                # print(j)
                mystr += str(j)
        return mystr
    
    def oneline_ai(self,arr2D):
        mystr = ""
        for i in arr2D:
            for j in i:
                mystr += str(j)

        if self.flagWb:
            mystr = mystr.replace("1", "x").replace("2", "1")
        else:
            mystr = mystr.replace("2", "x") 
        
        return mystr    
    
    
    def gibo2db(self):
        arr_i,arr_j =self.getGibo()
        win = -1
        if len(arr_i)%2 ==0:
            win = 2
        else:
            win = 1
        self.win = win
            
        for i in range(len(arr_i)):
            ii = arr_i[i]
            jj = arr_j[i]
            if self.flagWb:
                self.arr2D[ii][jj]=1
            else:
                self.arr2D[ii][jj]=2 
            str = self.oneline(self.arr2D)
            str_ai = self.oneline_ai(self.arr2D)
            
            self.gibo.append(str[0:40])
            self.gibo_ai.append(str_ai[0:40])
            self.ans.append(ii*20+jj)
            
            print(i,ii,jj,str[0:40],str_ai[0:40],ii*20+jj,win)
            
            self.flagWb = not self.flagWb

        
        

if __name__ == '__main__':
    rg = RaoGibo()

    
    