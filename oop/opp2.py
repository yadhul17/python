# class animal():
#     def __init__(self,name):
#         self.name=name

# class dog(animal):
#     def __init__(self,name,breed):
#         super().__init__(name)
#         self.breed=breed
#     def sound(self):
#         print("wooof")
#     def display(self):
#         print(self.name,self.breed)
    
    
# dogs=dog('arjun','lab')
# dogs.display()
# dogs.sound()


# abstract method
from abc import ABC,abstractmethod
class vehicle(ABC):
    @abstractmethod
    def tyre(self):
        print("tyre")
class car(vehicle):
    def tyre(self,no):
        self.no=no
        print(self.no)
class bike(vehicle):
    def tyre(self):
        print("tyre")
bmw=car()
bmw.tyre(4)
ns=bike()
ns.tyre()

