# from sample1 import *
# fun()
# fun2()
# print(fun3(2,6))

# import datetime

# x = datetime.datetime.now()

# print(x.year)
# print(x.second)
# print(x.strftime("%B"))
# print(x.strftime("%D"))
# print(x.strftime("%m"))
try:
    f=open('sample1.txt','x')
except:
    print("file exists")
f=open('sample1.txt','w')
f.write('hello')
f=open('sample1.txt','w')
for i in range(10):
 f.write(str(i)+'\n ')
