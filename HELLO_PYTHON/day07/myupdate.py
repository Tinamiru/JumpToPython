import pymysql

conn = pymysql.connect(host='localhost', port=3305, user='root', password='python', db='python', charset='utf8')

if conn.open:
    cursors = conn.cursor(pymysql.cursors.DictCursor)
    print("connect success\n")
e_id = 3
e_name = 4 
sex = 4
addr = 4

 
sql = f"""
        UPDATE emp
           set e_name = {e_name},
               sex = {sex},
               addr = {addr}
         WHERE e_id = {e_id}
      """
cnt = cursors.execute(sql)

if cnt > 0:
    print(" check the generated query result is success")

conn.commit()
conn.close()