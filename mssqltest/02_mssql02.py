import dbconn as db
# Some other example server values are
 
conn = db.dbconn()
cursor = conn.cursor()
sql = '''if not exists (select * from sysobjects where name='blog' and xtype = 'U')

   create table blog (
   id int identity not null primary key,
   title nvarchar(50) not null,a
   content nvarchar(100) not null,
   img_path nvarchar(50)
)'''
cursor.execute(sql)
conn.commit()
conn.close()