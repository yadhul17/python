import random
b=[{'bookid':1,'bookname':'yadhu','author':'my','price':20,'rent':False},{'bookid':2,'bookname':'anay','author':'my','price':20,'rent':False}]
a=[]

while True:
    print(''' 1.admin
             2.user''')
    ch=int(input("enter your choice:"))
    name1=1234
    if(ch==1):
        name=input("enter the name:")
        password=int(input("enter the password:"))
        if(password==name1):
            print("login succesfully")
            while True:
                 print(''' 1.add books
                    2.delete books
                       3.serch boooks
                       4.update books
                       5.view
                       6.exit''')
                 ch=int(input("enter your choice:"))
                 if ch==1:
                     bookid=int(input("enter the book id:"))
                     bookname=(input("enter the book name:"))
                     author=(input("enter the book author:"))
                     price=int(input("enter the book price:"))
                     b.append({'bookid':bookid,'bookname':bookname,'author':author,'price':price})
                 elif(ch==5):
                     for s in b:
                         print(s)
                 elif(ch==3):
                      flag=0
                      bid=int(input("enter the book id to serch:"))
                      for s in b:
                          if s['bookid']==bid:
                              flag=1
                      if flag==1:
                          print("book available")
                          print("book name",s.get('bookname'))
                      else:
                           
                        print("book not available")
                 elif ch==2:
                     bid=int(input("enter the bookid for deletion: "))
                     for s in b:
                         if s['bookid']==bid:
                             b.remove(s)
                 elif ch==6:
                     print("exiting.......")
                     break
                 
                         
                     
                     
                                              

                     
                

    elif ch==2:
     while True:
      print('''1.create new aaccount" 
                 2.signin
                 3.exit
            

        ''')
      c=int(input("enter your choice:"))
      if c==1:   
            username=input("enter your emailid")
            phonenumber=int(input("enter your phonenumber:"))
            password=int(input("enter your password:"))
            a.append({'username':username,'phonenumber':phonenumber,'password':password,'books':[]})
            print(a)
      elif c==2:
         username=input("enter your emailid:")
         password=int(input("enter the password:"))
         for s in a:
            flag=0
            if s['username']==username and s['password']==password:
                flag=1
            if flag==1:
                print("login suuccesfullly")
                while(True):
                 print('''1.serch
                           2.view userdetails
                           3.show books
                            4.lend book
                             5.exit''')
                 ch=int(input("enter the option:"))
                 if ch==1:
                    bookid=int(input("enter the bookid:"))
                    for s in b:
                        if s['bookid']==bookid:
                            print(s.get('bookname'),"is avaiable")
                        else:
                           print("book not available:")
                 elif ch==2:
                    for s in a:
                        print(s)
                 elif ch==3:
                     for s in b:
                         print(s)
                 elif ch==4:
                    bkid=int(input("enter the bookid:"))

                    for s in b:
                      if s['bookid']==bkid and s['rent']==True:
                             s['rent']=False
                          
                              
                             z=s.get('bookname')
                             a.append({'books':[z]})
                    else:
                              print("book not available")
                 elif ch==5:
                     print("exiting...")
                     break 
                                    
                         

                     
                
            elif c==3:
                print("exiting....")
                break
             
                
            
        

            




    
    