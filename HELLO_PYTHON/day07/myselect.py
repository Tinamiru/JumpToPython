import pymysql

conn = pymysql.connect(host='localhost', port=3305, user='root', password='python', db='python', charset='utf8')

if conn.open:
    cursors = conn.cursor(pymysql.cursors.DictCursor)
    print("connect success\n")

sql = """
        select e_id as 아이디,
               e_name as 이름,
               sex as 성별,
               addr as 주소
          from emp
      """
cursors.execute(query=sql)

data = cursors.fetchall()
for record in data:
    print(record) 

conn.close()