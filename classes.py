# class car:
    
#     def __init__(self,color,mileage):
#         self.color = color
#         self.mileage = mileage
        

# car1 = car("blue",20000)
# car2 = car("red",30000)

# for car in (car1,car2):
#     print(car.color + " Has " + str(car.mileage))
    

# class dog: 
#     species="sdgjf"
    
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def speak(self,sound):
#         return self.name + " Makes sound " + sound

# class goldenr(dog):
    
#     def speak(self,sound="Bark"):
#         return super().speak(sound)

# dog1= goldenr("Sally",9)

# print(dog1.speak())

# class vechicle: 
    
#     def __init__(self,name,mileage,capacity):
#         self.name = name
#         self.mileage = mileage
#         self.capcity = capacity
    
#     def fair(self):
#         return self.capcity * 200

# class bus(vechicle):
#     def fair(self):
#         return super().fair() + 100

# buss=bus("A bus",34571,23)
# print(buss.fair())

class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

class Developer(Employee):
    raise_amt = 1.1
    
    def __init__(self,lang,first,last,pay):
        super().__init__(first,last,pay)
        self.lang = lang

class Manager(Employee):
    def __init__(self, first, last, pay,employees=None):
        super().__init__(first, last, pay)
        # self.employees = employees
        
        if employees == None:
            self.employees = []
        else:
            self.employees = employees
            
    def addEm(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
        
    def delEm(self,em):
        if em in self.employees:
            self.employees.remove(em)
    
    def showEmp(self):
        for emp in self.employees:
            print( "--> " + emp.fullname())
            


dev_1 = Developer("Python",'Corey', 'Schafer', 50000)
dev_2 = Developer("Java",'Test', 'Employee', 60000)
mag1= Manager("Bob","Bobby",1345890,[dev_1])

# print(dev_1.email)
# print(dev_1.pay)
# print(dev_1.apply_raise())
# print(dev_1.pay)
print(mag1.employees)
mag1.addEm(dev_2)
print(mag1.showEmp())



