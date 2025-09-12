# class synnefo:
#     def pyhton():
#         print("python")
#     def dm():
#         print("dm")
# student=synnefo
# student.pyhton()
# student.dm()

# class synefo:
#     def __init__(self):
#         self.name=input('enter the name:')
#         self.email=input("enter  the email:")
#     def python(self):
#         print("python",self.name,self.email)
#     def mearn(self):
#         print("mearn",self.name,self.email)
# student1=synefo()



# student1.python()
# student2=synefo()
# student2.mearn()

# class synefo:
#     def __init_(self,branch):
#         self.name=input('enter the name:')
#         self.email=input("enter  the email:")
#         self.branch=branch
#     def python(self):
#         print("python",self.name,self.email,self.branch)
#     def mern(self):
#         print("mern",self.name,self.email,self.branch)
# student1=synefo('ekm')
# student1.python()
# student2=synefo('tvm')
# student2.mern()



# single inheritance

# class synnefo:
#     def python():
        
#         print("python")
#     def mern():
#         print("mern")
# class novavi(synnefo):
#     def dm():
#         print("dm") 
# std1=novavi
# std1.dm()
# std1.mern()
# std1.python()


    
# multiple inheritance

# class train:
#     def travel_train():
#         print("train")
# class boat:
#     def travel_metro():
#         print("boat")
# class person(train,boat):
#     def travel():
#         print("travel")
# obj= person
# obj.travel_metro()
# obj.travel_train()
# obj.travel()

# multilevel iheritance

# class school:
#     def school():
#         print("school")
# class classrooms(school):
#     def classroom():
#         print("classroom")
# class student(classrooms):
#     def student():
#         print("student")
# obj=student
# obj.school()
# obj.student()
# obj.classroom()

# hirachical inheritance
# class synefo:
#     def synnefo():
#         print("syneffo")
# class studentt(synefo):
#     def student():
#         print("student")
# class teacherss(synefo):
#     def teachers():
#         print("teachers")

# obj1=studentt
# obj2=teacherss
# obj1.synnefo()
# obj1.student()
# obj2.synnefo()
# obj2.teachers()
    

# list conprihension
# l=[1,2,3,4,5,6]
# square=[x**2 for x in l]
# print(square)

# l=[1,2,3,4,5,6,7]
# even=[x for x in l if x%2==0]
# print(even)
# import copy
# a=[1,2,4,[5,6]]
# b=a.copy()
# b[3][1]=10
# print(b)
# print(a)
# b=copy.deepcopy(a)
# b[3][1]=4
# print(b)
# # print(a)
# class A:
#     def fun(self):
#         print("fun")

# class B(A):
#     def fun(self):
#         super().fun()
#         print("funb")

# obj = B()
# obj.fun()

class a:
    def __init__(self):
        print("std")
class b(a):
    def __init__(self):
        super().__init__()
        print("teacher")
obj=b()









