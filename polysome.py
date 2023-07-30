class complex:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        
    def __add__(self,other):
        real_part= str(self.a+other.a)
        img_part=str(self.b+other.b)
        print(real_part+'+i'+img_part)
        
    def __sub__(self,other): 
        real_part= str(self.a-other.a)
        img_part=str(self.b-other.b)
        print(real_part+'+i'+img_part)
        
num1=complex(4,5)
num2=complex(2,3)
num1.__add__(num2)
num1.__sub__(num2)

class A: 
    def __init__(self) -> None:
        print("class a")
        
    def display(self):
        print("Inside A")
        
    def override(self):
        print("Inside class A")
        
class B(A):
    def __init__(self,a) -> None:
        self.a=a
        print("Class b")
        
    def display(self,a):
        print("Inside B")
    
    def override(self):
        print("Inside class B")
        
print(B.__mro__)
b=B(2)
a=A()
a.display()
b.display(2)
b.override()