import sqlite3
con=sqlite3.connect('new.db')
cur=con.cursor()
cur.execute("create table  if not exists user(id int primary key ,name text,email text)")
# cur.execute("alter table user rename to table1 ")
# cur.execute("insert into user values(3,'dssf','yadhu@123')")
# con.commit()
cur.execute("create table  if not exists marklist(id int primary key,mal int,eng int,mat int,bio int)")
# cur.execute("insert into marklist values(3,'60','50','40','60')")
# con.commit()
cur.execute("select user.id,user.name,marklist.mal,marklist.eng,marklist.mat,marklist.bio from user join marklist on user.id=marklist.id ")
data=cur.fetchall()
for i in data:
    print(i)










