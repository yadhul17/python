import sqlite3
conn = sqlite3.connect('task.db', detect_types=sqlite3.PARSE_DECLTYPES)
cur = conn.cursor()
cur.execute('create table  if not exists task(id int primary key,name text,desc text, complete boolean   default 0)')
while True:
    print('''1.add task
             2. display
          3.update task
          4.filtter
          5.delete
          6.exit''' )
    ch=int(input("enter your choice"))
    if ch==1:
        id=int(input("enter the id no:"))
        name=input("enter the name:")
        desc=input("enter the desc:")
        task=input("enter the task:")
        if task in ('true','1'):
            taskval='1'
        else:
            taskval='0' 

        cur.execute ('insert into task(id,name,desc,complete)  values(?,?,?,?)',(id,name,desc,taskval))
        conn.commit()
    if ch==2:
       data=cur.execute("select * from task")
       for i in data:
           print(i)
    if ch==3:
        idno=int(input("enter the id to edit:"))
        while True:
            print('''enter the column to edit:
                    1.name
                  2.desc
                  3.complte/not
                  4.exit''')
            cho=int(input("enter  the choice:"))
            if cho==1:
             newname=input("enter new name:")
             cur.execute("update task set name=? where id=?",(newname,idno))
             conn.commit()
            if cho==3:
             new=input("enter new satus (rue/false),(1/0)")
             cur.execute('upadte task set name=? where id=?',(name,idno))
             conn.commit()
            if cho==2:
             newdesc =("enter the desc:")
             cur.execute('upadte task set name=? where id=?',(newdesc,idno))
             conn.commit()
            if cho==4:
               break
    if ch==5:
           idn=int(input("enter the id to delete:"))
           cur.execute("delete from task where id=?",(idn,))
           conn.commit()
    if ch==4:
        status = input("Enter the status to filter by (0 / 1 / true / false): ")
        if status.lower() in ('true', '1'):
            val = '1'
        else:
            val = '0'
        cur.execute("SELECT id, name, desc, complete FROM task WHERE complete = ?", (val,))
        rows = cur.fetchall()
        print("Filtered tasks:")
        if not  rows:
            print("no such items")
        else:
          for row in rows:


        
            print(f"id={row[0]}, name={row[1]}, description={row[2]}, complete={row[3]}")
    if ch==6:
       break
          

                   

