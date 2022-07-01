import pymysql

conn = pymysql.connect(host='localhost', port=3305, user='root', password='python', db='python', charset='utf8')

if conn.open:
    cursors = conn.cursor(pymysql.cursors.DictCursor)
    print("connect success\n")

sql = """
        insert into emp(
            e_id,
            e_name,
            sex,
            addr)
        value(
            %s,%s,%s,%s
            );
      """
cnt = cursors.execute(sql, (7,7,7,7))
if cnt > 0:
    print("check query result : success")

conn.commit()
conn.close()