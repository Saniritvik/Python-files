class Student:
    schoolName="HSI"
    def __init__(self,studentName,studentAge):
        self.studentName = studentName
        self.studentAge = studentAge
    
    def __str__(self) -> str:
        returnString= "The name of the student is " + self.studentName + " and he is " + str(self.studentAge) + " Years old and is studying in " + self.schoolName
        return returnString
    
    def changeAge(self,newAge):
        self.studentAge = newAge
    
    def changeStudentSchool(self,newSchoolName):
        print("Instance method has been calalaled")
        self.schoolName = newSchoolName
    
    @classmethod 
    def changeSchool(cls,newSchoolName):
        Student.schoolName = newSchoolName
    
    @staticmethod    
    def holidayList():
        print("This is the static method because yes")
    
Student.holidayList()
studentObject=Student("Bobber is cool and yes",345789)
print(studentObject)
studentObject.changeAge(450)
print(studentObject)
Student.changeSchool("SUJO")
print(studentObject)
studentObject.changeStudentSchool("SDFJK")
print(studentObject)
studenterObject=Student("Grape",140238)
print(studenterObject)