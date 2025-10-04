import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    username='yadhul',
    password='@2005',
    database='yadhul'
)
cursor=mydb.cursor()
cursor.execute('create table if not exists employee(id integer ,name text, dept text)')
# cursor.execute("insert into employee values(1,'yadhu',4)")
mydb.commit()
# id=int(input("enter the id"))
# name=input("enter the name:")
# dept=input("enter the dept")
# cursor.execute('insert into employee values(%s,%s,%s)',(id,name,dept))
# mydb.commit()
cursor.execute('select * from employee')
data=cursor.fetchall()
print(data)
# cursor.execute('update employee set name=%s , id=%s where dept=%s',('anu',4,9))
# mydb.commit()
# cursor.execute('delete  from employee where id=%s',(3,))
# mydb.commit()




