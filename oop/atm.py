class atm:
   
  
   
   def __init__(self,balance=0,pinno=123):
      self.balance=balance
      self.pin=pinno
     
   def checkbalance(self,pin):
      if self.pin==pin:
       print("balance=",self.balance)
      else:
         print("enter the correct pin")
   def deposit(self,pin,amount):
      if self.pin==pin:
        self.balance=self.balance+amount
   def withdraw(self,pin,amount):
       if self.pin==pin:
          self.balance=self.balance-amount
      
         
obj=atm()
while True:
      print('''1.balance check
               2.deposit
                3.withdrawal
                4.exit''')
      ch=int(input("enter the choice"))
      if ch==1:
         pin=int(input("enter the pin no:"))
         obj.checkbalance(pin)
      if ch==2:
        
            amount=int(input("enter the amount to deposite:"))
            pin=int(input("enter the pin no:"))
            obj.deposit(pin,amount)
      if ch==3:
         amount=(int(input("enter the amount to withdraw:")))
         pin=int(input("enter the pin:"))
         obj.withdraw(pin,amount)
      if ch==4:
         print("exiting...")
         break





           
