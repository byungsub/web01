import dbconn as db 
# Some other example server values are

conn = db.dbconn()
cursor = conn.cursor()
sql = '''insert into blog values(?,?,?)'''
data = [('첫 번째 글제목', '첫 번째 글내용', '/static/blog/img/img01.png'),
        ('두 번째 글제목', '두 번째 글내용', '/static/blog/img/img02.png')]
cursor.executemany(sql,data)
conn.commit()
conn.close()