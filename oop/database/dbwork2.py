import sqlite3
con=sqlite3.connect('blood.db')
cur=con.cursor()
cur.execute('create table if not exists blood (id int primary key,name text,city text,bloodgroup text,phoneno int)')
# cur.execute('alter table blood add column age int'
#             )
while True:
     print('''1.add
             2.update
              3.display
           4.filtter
           5.exit''')
     ch=int(input("enter your choice:"))
     if(ch==1):
         n=int(input("number of donaters to add"))
         for i in range(n):
             id=int(input("enter the id:"))
             name=input("enter the name:")
             city=input("enter the city name:")
             bg=input("enter the bg:")
             phone=int(input("enter the phone no:"))
             weight=int(input("enter the weight:"))
             age=int(input("enter the aage:"))
             cur.execute('insert into blood values(?,?,?,?,?,?,?)',(id,name,city,bg,phone,weight,age))
             con.commit()
     if ch==3:
         cur.execute("select * from blood")
         data=cur.fetchall()
         
         print("{:<10}{:<10}{:<10}{:<10}{:<15}{:<10}{:<10}".format('id','name','city','phoneno','bloodgroup','weight','age'))
         for i in data:
           print("{:<10}{:<10}{:<10}{:<10}{:<15}{:<10}{:<10}".format (i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
     if ch==2:
         while True:
             print(''''1.name
                   2.city
                   3.bloodgrooup
                   4.phoneno
                 5.weight
                   6.age
                   7.exit'''
                   )
             c=int(input("enter the choice"))
             if c==1:
              idno=int(input("enter the id to update:"))
              newname=input("enter a new name:")
              cur.execute("upadte blood set name=? where id=?",(newname,idno))
              con.commit()
             if c==2:
              idno=int(input("enter the id to update:"))
              newcity=input("enter a new city name:")
              cur.execute("upadte blood set city=? where id=?",(newcity,idno))
              con.commit()
             if c==3:
              idno=int(input("enter the id to update:"))
              newbg=input("enter a new blood group:")
              cur.execute("upadte blood set bloodgroup=? where id=?",(newbg,idno))
              con.commit()
             if c==4:
              idno=int(input("enter the id to update:"))
              newno=int(input("enter a new name:"))
              cur.execute("upadte blood set phoneno=? where id=?",(newno,idno))
              con.commit()
             if c==5:
              idno=int(input("enter the id to update:"))
              newweight=int(input("enter a new weight:"))
              cur.execute("upadte blood set weight=? where id=?",(newweight,idno))
              con.commit()
             if c==6:
              idno=int(input("enter the id to update:"))
              newage=int(input("enter a new age:"))
              cur.execute("update blood set age=? where id=?",(newage,idno))
              con.commit()
             if c==7:
                print("exiting....")
                break
     if ch==4:
        idn=int(input("enter the id:"))
        cur.execute("select * from blood where id=?",(idn,) )
        d=cur.fetchall()
        print("{:<10}{:<10}{:<10}{:<10}{:<15}{:<10}{:<10}".format('id','name','city','phoneno','bloodgroup','weight','age'))
        for i in d:
           print("{:<10}{:<10}{:<10}{:<10}{:<15}{:<10}{:<10}".format (i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
     if ch==5:
        print("exiting......")
        break
        

