limit1=int(input("enter the limit:"))
limit2=int(input("enter the end limit:"))
sum=0
oddsum=0
evensum=0
for i in range (limit1,limit2+1):
    if i%2!=0:
        oddsum=+i
    else:
        evensum=+i
   
print(oddsum)
print(evensum)

