class Vehicale:
    def __init__(self,capacity,milege,name):
        self.capacity = capacity
        self.milege = milege
        self.name = name
        
    def fare(self):
        print("Fare="+" " + str(self.capacity*100))
    
    def __str__(self) -> str:
        returnString = "The details of the vehicale are" + " " + str(self.capacity) + " " + str(self.milege) + " " + str(self.name)
        return returnString

class Bus(Vehicale):
    def __init__(self, capacity, milege, name,type="Normal"):
        super().__init__(capacity, milege, name)
        self.type = type
    
    def typeCheck(self):
        if self.type == "Normal":
            super().fare()
        else:
            print("It is a school bus children travel for free!")

normalObject=Bus(348,9234,"Bus")
normalObject.typeCheck()
# busObject=Bus(348,9234,"School bus","School")
# busObject.typeCheck()
vehicaleObject= Vehicale(23489,1,"A big bus")
# vehicaleObject.fare()
print(normalObject.__class__.__name__)
print(isinstance(normalObject,Bus))
print(isinstance(normalObject,Vehicale))
print(isinstance(vehicaleObject,Bus))
print(isinstance(vehicaleObject,Vehicale))