from operator import delitem

cart = []


def addCart():
    numberOfItems = int(input("How many items do you want to add to cart?"))
    for i in range(numberOfItems):
        cartItem = input("What item do you want to add to cart?")
        quantity = int(
            input("How many of " + cartItem + " do you want to buy?"))
        cart.append(cartItem + "||" + str(quantity))


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
    print("Items found")
    print("Item name -- quanity")
    for item in cart:
        print(item.split("||")[0] + "- - -" + (item.split("||"))[1])
        totalOfItems += int(item.split("||")[1])
    print("Number of items --" + str(totalOfItems))


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
