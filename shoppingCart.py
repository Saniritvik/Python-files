

shoppingCart=["Apples","Vegis","Butter","Pancakes","Strawberry"]
ritviksCart=["a game", "Bike", "Fruit"]

def printAllElements(list):
    """
    prints all elements in a list
    """
    check=100
    for i in range(0,len(list)):
        print(list[i])

# Appending a certain element
def appendingFunction(youNeedthis,list):
    list.append(youNeedthis)

#Delteing an element
def deleteingFunction(youDontNeedThis,list):
    list.remove(youDontNeedThis)

#Find an element
def finder(list,value):
    """
    Finds a certain element specified in a list
    Returns true or false
    """
    if value in list:
        return True 
    else:
        return False

printAllElements(shoppingCart)
appendingFunction("Banana",shoppingCart)
printAllElements(shoppingCart)
deleteingFunction("Banana",shoppingCart)
printAllElements(shoppingCart)
printAllElements(ritviksCart)
x=finder(ritviksCart,"Bike")
print(x)