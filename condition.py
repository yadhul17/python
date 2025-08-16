# studentTime=710
# time=730
# if studentTime>time:
#     print("get out")
# else:
#     print("keep it up")

# num1=49
# num2=30
# if num1>num2:
#     print(num1,"is large")
# else:
#     print(num2,"is large")

# firstNumber=int(input("enter firstnumber:"))
# secondNumber=int(input("enter second number"))
# if firstNumber>secondNumber:
#     print(firstNumber,"is large")
# else:
#     print(secondNumber,"is large")

# num1=int(input("enter a number:"))
# num2=int(input ("enter a number"))
# if num1==num2:
#     print("two numbers are equal")
# elif num1>num2:
#     print(num1,"is large")
# else:
#     print(num2,"is large")

# mark=int(input("enter mark of student:"))
# a='mark:'
# if(mark>90):
#     print(a,"A")
# elif(mark>80):
#     print(a,"B")
# elif(mark>60):
#     print(a,"C")
# elif(mark>=40):
#     print(a,"D")
# else:
#     print("failed")    

# f = int(input("Enter first number: "))
# s = int(input("Enter second number: "))
# t = int(input("Enter third number: "))

# if f >= s:
#     if f >= t:
#         print(f, "is the largest")
#     else:
#         print(t, "is the largest")
# else:
#     if s >= t:
#         print(s, "is the largest")
#     else:
#         print(t, "is the largest")

# f = int(input("enter number"))
# s = int(input("enter number"))
# t = int(input("enter number"))

# if f > s:
#     if f > t:
#         print(f, "is large")
#     else:
#         print(t, "is large")
# else:
#     if s > t:
#         print(s, "is large")
#     else:
#         print(t, "is large")


  #1 coAmpany  decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
  #Ask user for their salary and year of service and print the net bonus amount
# year=int(input("enter the number of year"))
# salary=int(input("enter the salary"))
# bonus=0
# if year>5:
#     bonus=salary*(5/100)
# print("salary:",salary)
# print("year of service:",year)
# print("bonus:",bonus)
# print("netsalary:",(salary+bonus))

#2 Write a program to calculate the electricity bill (accept number of unit from user) according to the following criteria :
#              Unit                                                     Price  
# First 100 units                                               no charge
# Next 100 units                                              Rs 5 per unit
# After 200 units                                             Rs 10 per unit
# (For example if input unit is 350 than total bill amount is Rs2000)

# unit=int(input("enter the unit used:"))
# charge=0
# if unit<=100:
#     charge=0
# elif unit<=200:
#     charge=(unit-100)*5
# else:
#     charge=(unit-200)*10+(100*5)
# print (charge)



# Write a program to accept a number from 1 to 7 and display the name of the day like 1 for Sunday , 2 for Monday and so on.
# day=int(input("enter the dayno:"))
# if day==1:
#     print("sunday")
# elif day==2:
#     print("monday")
# elif day==3:
#     print("tuesday")
# elif(day==4):
#     print("wendsday")
# elif(day==5):
#     print("thursday")
# elif(day==6):
#    print("friday")
# elif(day==7):
#     print("saturday")
# else:
#     print("unknown")

# 5 ite a program to check whether the last digit of a number( entered by user ) is 
# divisible by 3 or not.

# num=int(input("enter the number"))
# r=num%10
# if(r%3==0):
#   print("divisible by 3")
# else:
#   print("not divisible by 3")

# 6   Find the largest among 3 numbers using elif statement ..

# a=40
# b=20
# c=30
# if(a>b and a>c):
#     print(" a is large")
# elif b>a and b>c:
#     print("b is large")
# else:
#     print("c is large")

# Write a program to accept the cost price of a bike and display the road tax to be paid according to the following criteria :
    
        # Cost price (in Rs)                                       Tax
        # > 100000                                                  15%
        # > 50000 and <= 100000                                     10%
        # <= 50000                                                  5%

# price=int(input("enter cost of bike"))
# if price<=50000:
#     print("road tax:",price*(5/100))
# elif price>50000 and price<=100000:
#     print("road tax=",price*(10/100))
# else:
#     print("road tax=",price*(15/100))

#  Accept any city from the user and display monument of that city.
#                   City                                 Monument
#                   Delhi                               Red Fort
#                   Agra                                Taj Mahal
#                   # Jaipur                              Jal Mahal

# city=(input("enter the city name:"))
# if city=='delhi':
#     print("red fort")
# elif city=='agra':
#     print("taj mahal")
# elif city=='jaipur':
#     print("jaimahal")
# else:
#     print("unknown")
          

