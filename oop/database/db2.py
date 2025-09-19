# import sqlite3

# con= sqlite3.connect('std2.db')
# cur = con.cursor()
# cur.execute('create table if not exists std2(id int primary key,name text,department text)')
# # cur.execute("insert into std2 values('2','adhu','ct')")
# con.commit()
# cur.execute("select * from std2 where name like('y%')")
# data=cur.fetchall()
# print(data)
# cur.execute("select * from std2 where name like ('%u')")
# da=cur.fetchall()
# print(da)
# cur.execute("select * from std2 order by name desc")
# d=cur.fetchall()
# print(d)


# import sqlite3

# con= sqlite3.connect('std2.db')
# cur = con.cursor()
# cur.execute('create table if not exists std3(id int primary key,name text,department text)')
# # cur.execute("insert into std3 values('4','anu','ee')")
# con.commit()
# cur.execute("select count(*) from std3")
# data=cur.fetchone()
# print(data)




import sqlite3

con= sqlite3.connect('std2.db')
cur = con.cursor()
cur.execute('create table if not exists employee(id int primary key,name text,salary int)')
# cur.execute("insert into employee values('6','you','6000.50')")
con.commit()
cur.execute("select count(*) from employee")
data=cur.fetchone()
print("cout",data)
cur.execute("select sum(salary) from employee")
data=cur.fetchone()
print("sum",data)
cur.execute("select max(salary) from employee")
data=cur.fetchone()
print("max",data)
cur.execute("select min(salary) from employee")
data=cur.fetchone()
print("min",data)
cur.execute("select avg(salary) from employee")
data=cur.fetchone()
print("avg",data)