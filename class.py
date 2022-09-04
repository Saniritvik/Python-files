from time import sleep


class person:
    counter=0
    def __init__(self,age,gender,name):
        person.counter=person.counter+1
        self.age = age
        self.gender = gender
        self.name = name
    
    arms=2
    legs=2
    height="4'9"
    heads=1
    
    def __str__(self) -> str:
        returnString = "This a person object whose name is" + " " + self.name + " and is a " + self.gender
        return returnString
    
    def __del__(self):
        person.counter=person.counter-1
        print("We have" + " " + str(person.counter) + " humans alive")
billyObject= person(11,"Male","Billy bob joe bob")
dudeObject=person(15,"Female","A human")
otherObject=person(43,"Male","Sammy")
uhObject=person(3278,"Male","EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
print(uhObject)
# print(dudeObject)
# print(billyObject)
# print(otherObject)
# del billyObject
# del dudeObject
# sleep(10)