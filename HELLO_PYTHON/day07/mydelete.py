import pymysql

conn = pymysql.connect(host='localhost', port=3305, user='root', password='python', db='python', charset='utf8')

if conn.open:
    cursors = conn.cursor(pymysql.cursors.DictCursor)
    print("connect success\n")

sql = """
        DELETE FROM emp
         WHERE e_id = 7
      """
cnt = cursors.execute(sql)

if cnt > 0:
    print(" check the generated query result is success")

conn.commit()
conn.close()