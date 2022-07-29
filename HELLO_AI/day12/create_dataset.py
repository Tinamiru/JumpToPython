class RaoGibo:
    
    def __init__(self):
        pass

    def getGibo(self, file_name):
        f = open(file_name, 'r')
        
        lines = f.readlines()
        
        arr_i = []
        arr_j = []
        
        del lines[0]
        
        for line in lines:
            arr_split = line.split(",")
            mylen = len(arr_split)
            if mylen == 3:
                i = int(arr_split[0])
                j = int(arr_split[1])
                arr_i.append(i)
                arr_j.append(j)
        f.close()
        return arr_i, arr_j


if __name__ == '__main__':
    rg = RaoGibo()
    arr_i, arr_j = rg.getGibo("0_0_1_2.psq")
    print(arr_i)
    print(arr_j)
