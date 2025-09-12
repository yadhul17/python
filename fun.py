# a=10
# def sample():
#     a=11
# sample()
# print(a)

# def add(a,b):
#     print(a+b)
    
# a=int(input("enter number:"))
# b=int(input("enter number:"))
# add(a,b) 

# def even(a):
#     if a%2==0:
#         print("even")
#     else:
#         print("odd")
# a=int(input("enter a number:"))


# even(a)
# def add(a,b):
#     return a+b
# a=int(input("enter:"))
# b=int(input("enter:"))
# result=add(a,b)
# print('sum',result)

# def num(a,b,c):
#     return a,b,c
# a=1
# b=2
# c=3
# r=num(a,b,c)
# x,y,z=num(a,b,c)
# print(r)
# print(x,y,z)


# def std(name,age):
#      print(name,age)
# std(name="yadhu",age=13)
# def student(*arg):
#     print(arg)
# student(1,2,3)
# student('yadhu',34543)
# student(1)
# student()

# def std(name,age,course='python'):
#     print(name,age,course)
# std("yadhu",13)

def std(**arg):
    print(arg)
std(name='yadhu',age=24,course='python')