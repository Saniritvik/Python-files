# class Test:
#     x = 10 #Class variable
    
#     def __init__(self) -> None:
#         self.x=1 #Instance variable
#         print("Inside constructor,",self.x)
    
#     def __str__(self) -> str:
#         return "Hello!"

# object = Test()
# print(object)
# print("Outside",object.x)

# object.x=5
# print(object.x)

# print(Test.x)
# Test.x=6
# print(Test.x)

# d=Test()
# print(d.x)
# print(Test.x)

# class A: 
#     def __init__(self) -> None:
#         self.x=1
#         self.y=2
        
#     def display(self):
#         print("x is",self.x)
#         print("y is",self.y)

# a=A()
# a.display()

# class A:   
#    def display(self):
#        self.x=1
#        self.y=2
#        print(self.x)
#        print(self.y)
# a=A()
# a.display()

# class A:   
#    c=5
#    def __init__(self) -> None:
#        self.x=1
#        self.y=2
#        print("x in constructor",self.x)
#        print("y in constructor",self.y)
#        print("c in class",A.c)
   
#    def display(self):
#        self.x=2
#        self.y=3
#        A.c=6
#        print("x in display",self.x)
#        print("y in display",self.y)
#        print("c in class",A.c)
# a=A()
# a.display()

# b=A()
# b.display()

# class A:   
#    c=5
#    def __init__(self) -> None:
#        self.x=2
#        self.y=3
#    def display(self):
#        print("x in display",self.x)
#        print("y in display",self.y)
#        print("c in class",A.c)
# a=A()
# print(A.c)
# print(a.x)

# class A: 
#     def __init__(welcome) -> None:
#         welcome.x=14
#         welcome.y=25
        
#     def display(hello):
#         print(hello.x)
#         print(hello.y)

# a=A()
# a.display()

# Self is a reference to an object that is calling the method

# class B:
#     y=2
#     def __init__(self) -> None:
#         self.x=1
    
#     def getItem(self):
#         pass
    
#     def setItem(self):
#         pass
# b=B()
# print(b.__dir__())

# class A: 
#     def __init__(self) -> None:
#         self.x=14
#         self.y=25
        
#     def display(self):
#         print(self.x)
# a=A()
# print(a.__dict__)

# class A: 
#     def __init__(self) -> None:
#         self.x=1
#         self.__y=2
        
#     def display(self):
#         print("Y is",self.__y)
    
#     def updatey(self,y):
#         self.__y=y
# a=A()
# a.display()
# a.updatey(6)
# a.display()

# class A: 
#     def __init__(self) -> None:
#         self.x=1
#         self.__y=2
        
#     def display(self):
#         print("Y is",self.__y)
    
#     def updatey(self,y):
#         self.__y=y
# a=A()
# del a
# a.display()

# class A: 
#     def __init__(self) -> None:
#         self.x=1
#         self.__y=2
        
#     def display(self):
#         print("Y is",self.__y)
    
#     def updatey(self,y):
#         self.__y=y
        
#     def __del__(self):
#         print("Deleted.")

# # a=A()
# # del a

# # class B:
# #     pass
# # print(isinstance(B,A))

# class A: 
#     def __init__(self) -> None:
#         self.x=1
#         self.__y=2
#         print("Parent constructer called")
        
#     def display(self):
#         print("Y is",self.__y)
#         print("Parent display called")
    
#     def updatey(self,y):
#         self.__y=y
#         print("Parent cupdatey called")

# class B(A): 
#     def __init__(self) -> None:
#         super().__init__()
#         print("Child constructer called")

# b=B()

# class A: 
#     def __init__(self) -> None:
#         self.x=1
#         self.__y=2
#         print("Parent constructer called")
        
#     def display(self):
#         print("Y is",self.__y)
#         print("Parent display called")
    
#     def updatey(self,y):
#         self.__y=y
#         print("Parent cupdatey called")

# class B(A): 
#     def __init__(self) -> None:
#         A()
#         print("Child constructer called")

# b=B()

# class A(object):
#     def __init__(self) -> None:
#         print("Parent")
        
#     def display(self):
#         print("Inside class A")
# class B(A):
#     def __init__(self) -> None:
#         print("Child")
        
#     def display(self):
#         super().display()
#         print("Inside class B")
        
# b=B()
# b.display()


# class Shape: 
#     def display(self,side):
#         print("The area is " + str(side * side))
        
# class Square(Shape): 
#     def __init__(self) -> None:
#         self.side = int(input("Give me a number"))
#         super().display(self.side)
        
# sq=Square()

# class D: #Great grand parent
#     pass

# class A(D): #Grand parent
#     def __init__(self) -> None:
#         print("Class A")

# class B(A): #Parent
#     def __init__(self) -> None:
#         print("Class B")

# class C(B): #Child
#     pass

# print(C.__mro__)

# class Q:
#     pass
# print(Q.__mro__)

# class Animal:
#     def __init__(self) -> None:
#         print("Animal")

# class Reptile(Animal):
#     def __init__(self) -> None:
#         super().__init__()
#         print("Reptile")
        
#     def animalPrinting(self,n):
#         print("Reptile ",n)

# class Crocodile(Reptile):
#     def __init__(self,n) -> None:
#         super().__init__()
#         super().animalPrinting(n)
#         print("Crocodile")

# croc=Crocodile(5)

# class A: 
#     pass

# class B(A):
#     pass

# class C(A): 
#     pass

# print(C.__mro__)
# print(B.__mro__)

from abc import ABC,abstractclassmethod
class Shape(ABC): 
    @abstractclassmethod
    def area(self): 
        pass

class Square(Shape): 
    def area(self,a): 
        print(a * a)
        
class Rectangle(Shape): 
    def area(self,b,l): 
        print(b * l)
        
class Triange(Shape):
    def area(self,b,h):
        print(b * h // 2)
        
s= Square()
r=Rectangle()
t=Triange()
s.area(5)
r.area(5,2)
t.area(20,2)