import sqlite3

con= sqlite3.connect('employe.db')
cur = con.cursor()
cur.execute('create table if not exists employe(id int,name text,department text)')
while True:
    print('''employe management system
          
             1.add employe
             2.display
             3.update
             4.filter
             5.delete
             6.exit''')
    ch=int(input("enter your choice:"))
    if ch==1:
        no=int(input("enter the number of employe to add:"))
        for i in range(no):
            id=int(input("enter your id:"))
            name=input("enter your name:")
            department=input("enter your department:")
            cur.execute("INSERT INTO employe VALUES (?, ?, ?)", (id, name, department))
            con.commit()
    if ch==2:
         cur.execute('select * from employe')
         data=cur.fetchall()
         print("{:<10} {:<10} {:<10}".format('id','name','department'))
         for i in data:
             print("{:<10} {:<10} {:<10}".format(i[0],i[1],i[2]))
    if ch==3:
        while True:
            
            print('''1.name
                  2.department
                  3.exit''')
            
            c=int(input("what you want to update:"))
            
            if c==1:
                idno=int(input("enter the id to update:"))
                

                newname=input("enter the new name:")
                cur.execute('update employe set name=? where id=?',(newname,idno))
                con.commit()
            elif(c==2):
                idno=int(input("enter the id to update:"))
                newdept=input("enter the new department:")
                cur.execute('update employe set department=? where id=?',(newdept,idno))
                con.commit()
            elif c==3:
                print("exiting....")
                break
            else:
                print("invalid input.....")
    if ch==4:
        while True:
            print('''deapartments
                     1.s
                     2.h
                     3.exit''')
            choice=int(input("enter your choice:"))
            if choice==1:
                dept='s'
                cur.execute("select * from employe where department=?",(dept,))
                data=cur.fetchall()
                print("{:<10} {:<10} {:<10}".format('id','name','department'))
                for i in data:
                    print("{:<10} {:<10} {:<10}".format(i[0],i[1],i[2]))
            elif choice==2:
                dept='h'
                cur.execute("select * from employe where department=?",(dept,))
                data=cur.fetchall()
                print("{:<10} {:<10} {:<10}".format('id','name','department'))
                for i in data:
                    print("{:<10} {:<10} {:<10}".format(i[0],i[1],i[2]))
            elif choice==3:
                print("exiting from filter....") 
                break
    elif ch==5:
        i=int(input("enter the id to delete:"))
        cur.execute('delete  from employe where id=?',(i,))
        con.commit()

    elif ch==6:
        print("exiting......")
        break

            



