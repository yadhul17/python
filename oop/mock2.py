b=[]
l=[]
def addstaff(id,name,dept):
    
     b.append({'staffid':id,'staffname':name,'department':dept})

   

    
        



while True:
    print('''1.add staf
          2.view all staf
          3.edit staff
          4.filter staf on department
          5.exit''')
    ch=int(input("enter your choice:"))
    if ch==1:
        id=int(input("enter your id:"))
        name=input("enter your name:")
        dept=input("enter your department")
        addstaff(id,name,dept) 
    if ch==2:
        for i in b:
            print(i)
    if ch==4:
        dep = input("Enter your department: ")
        flag = False
   

        for i in b:
            if i.get('department')== dep:
                flag = True
                l.append(i.get('staffname'))
                
           

        if flag:
            print("Staff is available")
            for i in l:
                print(i)
            
        
        else:
            print("Staff is not available")
    if ch == 3:
     while True:
        print('''
              1. Name
              2. Department
              3. Exit
        ''')
       
        choice=int(input("enter the choice:"))
        if choice == 1:
           
            idn=int(input("enter the id to update:"))
            new_name = input("Enter the new name: ")
            for staff in b:
                if staff.get('staffid') == idn:
                    staff['staffname'] = new_name     
        elif choice == 2:
            
            idn=int(input("enter the id to update:"))
            new_department = input("Enter the new department: ")
            for staff in b:
                if staff.get('staffid') == idn:
                    staff.update(department=new_department)
        elif choice==3:
            print("Exiting update menu.")
            break
        

    if ch==5:
        print("exiting....")
        break
            

                     



       


