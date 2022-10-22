import dbconn as db 
# Some other example server values are

conn = db.dbconn()
cursor = conn.cursor()
sql = '''insert into blog values
(N'첫 번째 글제목', N'첫 번째 글내용', '/static/blog/img/img01.png'),
(N'두 번째 글제목', N'두 번째 글내용', '/static/blog/img/img02.png')'''
cursor.execute(sql)
conn.commit()
conn.close()