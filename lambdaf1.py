# add=lambda a,b:a+b
# print(add(2,3))

# square=lambda a:a*a
# num =int(input("enter a number:"))
# print(square(num))


# check=lambda a:a%2
# num=int(input("enter a number:"))
# z=check(num)

# if z==0:
#     print("even")
# else:
#     print("odd")




# map

# num=[1,2,3,4,5,6]
# l1=list(map(lambda x:x*x,num))
# print(l1)

# def product(x):
#      for i in x:
#        l=list(i*i)
#      return l
# print(product(num))

# def product(x):
#     return x*x
# l=list(map(product,num))
# print(l)

# filter

# filterd_list=list(filter(lambda x:x%2==0,num))
# print(filterd_list)

# def filtter(x):
#     return x%2==0
# l=list(filter(filtter,num))
# print(l)

# from functools import reduce
# result=reduce(lambda x,y:x+y,num)
# print(result)

