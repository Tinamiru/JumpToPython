import pymysql

class DaoStock:
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='python',port=3305,
                       db='python', charset='utf8')
 
        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)

    
    def insert(self,s_code,ymd,s_name,price):
        sql = f"""
            insert into stock
                (s_code,ymd,s_name,price)
            values 
                ('{s_code}','{ymd}','{s_name}','{price}')
        """
        cnt = self.curs.execute(sql)
        self.conn.commit()
        return cnt

    
    def __del__(self):
        self.curs.close()
        self.conn.close()
        
        
if __name__ == '__main__':
    de = DaoStock()
    cnt = de.insert(1,1,1,1)
    print("cnt",cnt)
    
    
    
    
    