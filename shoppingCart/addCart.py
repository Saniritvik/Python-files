from operator import delitem
from items import viewItems
cart = []

cart=[]
def addCart():
    totalPrice=0
    index,totalItems,itemsPrice = viewItems()
    numberOfItems = int(input("How many items do you want to add to cart?"))
    for i in range(numberOfItems):
        cartItem = int(input("What item do you want to add to cart?(Enter the index number)"))
        if cartItem > 0 and cartItem <= index:
            Item=totalItems[cartItem-1]
            quantity = int(input("How many of " + Item + " do you want to buy?"))
            cart.append(Item + "||" + str(quantity) + "||" + str(itemsPrice[cartItem-1]))
        else:
            print("Go back to kindergarden and LEARN NUMBERS")



def delEntireCart(fileName):
    yn = input("User are you sure you want to delete the enitire cart? (y/n)")
    if yn == "y":
        print("Deleting cart")
        filePointer = open(fileName, mode="w")
        cart.clear()
    elif yn == "n":
        print("Okay")
    else:
        print("That is not a valid answer")
        delEntireCart()


def viewCart():
    totalOfItems = 0
    totalPrice = 0
    print("Items found")
    print("Item name -- quanity")
    for item in cart:
        print(item.split("||")[0] + "- - -" + (item.split("||"))[1])
        totalOfItems += int(item.split("||")[1])
        totalPrice += int(item.split("||")[1])*float(item.split("||")[2])
    print("Number of items --" + str(totalOfItems))
    print("Total price equal to:" + str(totalPrice) + " now stop shopping!")



def deleteItem():
    viewCart()
    delItem = input("What is the item you want to delete?")
    cart.remove(delItem)


def saveItems(fileName):
    filePointer = open(fileName, mode="w")
    if len(cart) > 0:
        for item in cart:
            filePointer.writelines(item + "\n")
    filePointer.close()


def loadCart(fileName):
    cart.clear()
    filePointer = open(fileName, mode="r")
    fileData = filePointer.readlines()
    for line in fileData:
        cart.append(line.strip())
    filePointer.close()


def delScreen():
    print(chr(27) + "[2J")


def displayScreen(screenName):
    print("*********************************")
    print("*********************************")
    print("**********" + screenName + "************")
    print("*********************************")
    print("*********************************")
