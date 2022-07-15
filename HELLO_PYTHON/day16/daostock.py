import pymysql


class DaoStock:

    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='python', port=3305,
                       db='_stock_old', charset='utf8')
 
        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)

    def getPrice(self, s_name):
        ret = []
        sql = f"""
            select s_code,ymd,s_name,price from stock_sync_0121
            where
            s_name = '{s_name}'
        """
        self.curs.execute(sql)
        rows = self.curs.fetchall()
        for r in rows:
            ret.append(r['price'])
        return ret
    
    def selects(self):
        sql = f"""
            select * from stock_sync_0121
        """
        self.curs.execute(sql)
        ret = self.curs.fetchall()
        return ret
    
    def __del__(self):
        self.curs.close()
        self.conn.close()

        
if __name__ == '__main__':
    de = DaoStock()
    list = de.selects('삼성전자')
    print("list", list)
    
