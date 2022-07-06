import pymysql


class DaoEmp:

    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='python', port=3305,
                       db='python', charset='utf8')
 
        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)
        
    def selects(self):
        sql = "select * from emp"
        self.curs.execute(sql)
        rows = self.curs.fetchall()
        return rows
    
    def select(self, e_id):
        sql = "select * from emp where e_id = " + e_id
        self.curs.execute(sql)
        rows = self.curs.fetchall()
        return rows[0]
    
    def insert(self, e_name, sex, addr):
        sql = f"""
            insert into emp(
            e_name, sex, addr)
            values('{e_name}','{sex}','{addr}')
        """
        cnt = self.curs.execute(sql)
        self.conn.commit()
        return cnt
    
    def update(self, e_id, e_name, sex, addr):
        sql = f"""
            update emp set e_name = '{e_name}', sex = '{sex}', addr = '{addr}'
            where e_id = '{e_id}'
        """
        cnt = self.curs.execute(sql)
        self.conn.commit()
        return cnt
    
    def delete(self, e_id):
        sql = f"""DELETE from emp where e_id = {e_id}"""
        cnt = self.curs.execute(sql)
        self.conn.commit()
        return cnt
    
    def __del__(self):
        self.curs.close()
        self.conn.close()
        
        
if __name__ == '__main__':
    de = DaoEmp()
    # list = de.selects()
    # select = de.select("1");
    # cnt = de.insert('13', '13', '13')
    # cnt = de.update("13", "1", "1", "1")
    cnt = de.delete("13")
    print("cnt", cnt)
