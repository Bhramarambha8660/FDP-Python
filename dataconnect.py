import mysql.connector as conn
con=conn.connect(user='root',password='root',database='skit',host='localhost')
print(con)
cursor=con.cursor()
cursor.execute('select * from staff')
for row in cursor.fetchall():
    print(row)