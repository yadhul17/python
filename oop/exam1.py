class Rectangle:
    
    def __init__(self):
        w=int(input("enter a value:"))
        h=int(input("enter the value:"))
        if w<=0 or h<=0:
             w=int(input("enter a value:"))
             h=int(input("enter the value:"))
        else:
         self.width=w
         self.height=h

       


    def perimeter(self):
        return (self.height+self.width)*2
    def area(self):
        return (self.width*self.height)
    def display(self,a,b):
        area=a
        perimeter=b
        print("area=",area)
        print("perimeter=",perimeter)

r1 = Rectangle()
a=r1.area()
b=r1.perimeter()
r1.display(a,b)



        