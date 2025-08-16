student=[]
c=[]

while True:
    print(''' 1.addstudent
            2.delete
            3.display
            4.serch
            5.exit''')
    ch=int(input("enter your choice"))
    if ch==1:
        name=input("enter name of student:")
        adno=int(input("enter the addmission number:"))
        age=int(input("enter the age:"))
        clas=int(input("enter the class:"))
        student.append([name,age,clas,adno])
    
    elif ch==4:
         ad=int(input("enter the admission number of student:"))
         flag=0
         for sublist in student:
             if ad in sublist:
                   flag=1
         if flag==1:
             print("student is present")
         else:
             print("student is absent in list")
    elif  ch==2:
        name=(input("enter the name for delete from the list:"))

        for sublist in student:
            if name in sublist:
              print("removed" ,student.remove(sublist))
           
        

        
    elif ch==3:
        for i in student:
            print(i)
   
            
        
         
              

    
            
                

    elif ch==5:
        print("exiting....")
        break



       


