import pymysql


class DaoStock:

    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='python', port=3305,
                       db='_stock_old', charset='utf8')
 
        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)

    
    def selects(self):
        sql = f"""
            select * from stock_sync_0121
        """
        self.curs.execute(sql)
        rows = self.curs.fetchall()
        return rows
    
    def __del__(self):
        self.curs.close()
        self.conn.close()

        
if __name__ == '__main__':
    de = DaoStock()
    
