
import pymssql
server = 'WIN-LHRELIH802D'
user = 'iplan'
password = '1234qwerasdfzxcv!'
database = 'YZDQUOTE'
conn = pymssql.connect(server, user, password, database )


cursor = conn.cursor()

cursor.execute('SELECT    * FROM [m_employe]')
row = cursor.fetchall()
print(row)
conn.commit()