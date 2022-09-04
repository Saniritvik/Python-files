from functools import total_ordering


itemsFileName = "items.txt"
totalItems = []
itemsPrice = []


def itemsMenu():
    stop = False
    while not stop:
        itemsMenyEntry = int(input(
            "What do you want to do? \n 1 View items \n 2 Add new item \n 3 Delete item \n 4 exit to main menu \n"))
        if itemsMenyEntry == 1:
            viewItems()
        elif itemsMenyEntry == 2:
            addNewItem()
        elif itemsMenyEntry == 3:
            delItem()
        elif itemsMenyEntry == 4:
            stop = True
        else:
            print("NOT AN OPTION READ BETTER")


def viewItems():
    filePointer = open(itemsFileName, mode="r")
    itemsRead = filePointer.readlines()
    print("Here are your availble items")
    print("Index --- item name -- price")
    index = 1
    for lines in itemsRead:
        print(str(index) + "." + lines.split("||")
              [0] + "---" + str(lines.split("||")[1]), end=" ")
        totalItems.append(lines.split("||")[0])
        itemsPrice.append(lines.split("||")[1])
        index += 1
    print("")
    item = int(input("Choose the index to add item to cart"))
    print(totalItems[item-1])
    print(itemsPrice[item-1])


def addNewItem():
    filePointer = open(itemsFileName, mode="r+")
    readLines = filePointer.readlines()
    print(readLines)
    existItem = []
    for lines in readLines:
        existItem.append(lines.split("||")[0].lower())
    item = input("What do you want to add?")
    lowerd = item.lower()
    price = float(input("How much does it cost?"))
    print(existItem)
    print(lowerd)
    if lowerd in existItem:
        print("ADMIN ITS ALREADY THERE READ BRO, TRY AGAIN")
    else:
        filePointer.writelines("\n" + item + "||" + str(price))
        print("Item added")

def delItem():
    ## List all items in items, then what item to delete, remove item from item.txt
    filePointer = open(itemsFileName, mode="r")
    itemsRead = filePointer.readlines()
    filePointer.close()
    print("Here are your availble items")
    print("Index --- item name -- price")
    index = 1
    for lines in itemsRead:
        print(str(index) + "." + lines.split("||")
              [0] + "---" + str(lines.split("||")[1]), end=" ")
        totalItems.append(lines.split("||")[0])
        itemsPrice.append(lines.split("||")[1])
        index += 1
    item=int(input("What item do you want to delete?) (Enter index)"))
    if item > 0 and item <= index:
       itemsRead.pop(item-1)
       filePointer = open(itemsFileName, mode="w")
       filePointer.writelines(itemsRead)
    else:
        print("Bruh. The item was not found learn numbers")