from addCart import *
from items import *
mainScreenNames={
    1:"Ritvik",
    2:"Neeta",
    3:"Rishi"
}
    
fileNames={
    1:"Ritvik.txt",
    2:"Neeta.txt",
    3:"Rishi.txt"
}

def shoppingCartScreen(entry):
    stop = False
    while not stop:
        displayScreen("Home Screen")
        shoppingCartEntry=int(input("What do you want to do? \n 1 View cart \n 2 Delete something \n 3 Add something to cart \n 4 Save and exit to main menu \n 5 Delete THE ENTIRE CART"))
        if shoppingCartEntry == 1:
            delScreen()
            viewCart()
        elif shoppingCartEntry == 2:
            delScreen()
            deleteItem()
        elif shoppingCartEntry == 3:
            delScreen()
            addCart()
        elif shoppingCartEntry == 4:
            delScreen()
            saveItems(fileNames[entry])
            stop=True
        elif shoppingCartEntry == 5:
            delScreen()
            delEntireCart(fileNames[entry])

        else: 
            print("NOT AN OPTION READ BETTER")

def mainScreen():
    while True:
        displayScreen("User Screen")
        entry=int(input("WHO ARE YOU?? \n 1 Ritvik \n 2 Neeta \n 3 Rishi \n 4 EXIT \n 5 Admin"))
        menuNames=mainScreenNames.keys()
        if entry in menuNames:
            delScreen()
            print("Hello " + mainScreenNames[entry])
            loadCart(fileNames[entry])
            shoppingCartScreen(entry)
        elif entry == 4:
            delScreen()
            exit()
        elif entry == 5:
            delScreen()
            itemsMenu()
        else:
            delScreen()
            print("That person DOES NOT EXIST please try again")
            mainScreen()

mainScreen()
