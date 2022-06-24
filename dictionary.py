# namesAndDob={
#     "Bob":"01/31",
#     "Joe":"04/23",
#     "Rob":"07/22"
# }
# print(namesAndDob.keys())
robDict={
    "studentName":"Rob",
    "parent":"Rob mom",
    "examGrade":"89"
}
bobDict={
    "studentName":"Bob",
    "Parent":"Bob mom",
    "examGrade":"78"
}
bobAndRob={
    "Bob":bobDict,
    "Rob":robDict
}
# for key in bobAndRob.keys():
#     studentDict = bobAndRob[key]
#     print(studentDict["Student"])
names = bobAndRob.keys()
for i in names: 
    bobAndRob.setdefault()