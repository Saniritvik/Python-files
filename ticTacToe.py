import random
import time
## tic tac toe grid 
grid2={
    1:"#",
    2:"#",
    3:"#",
    4:"#",
    5:"#",
    6:"#",
    7:"#",
    8:"#",
    9:"#"
}

## Printing out the grd that is changing
def currentGrid():
    print("Current grid")
    print(grid2[1] + "|" + grid2[2] + "|" + grid2[3])
    print(grid2[4] + "|" + grid2[5] + "|" + grid2[6])
    print(grid2[7] + "|" + grid2[8] + "|" + grid2[9])

## Checking if a player already took a spot and filling the grid with the players provided places
def fillGrid(): 
    turn="x"
    ##Setting round to 0
    init()
    currentGrid()
    counter=0
    for i in range(1,10):
        filled=True
        while filled:
            xturn=int(input("Player " + turn + " where would you like to pick? (1-9)"))
            if grid2[xturn] == "o" or grid2[xturn] == "x":
                print("Another player has put their x/o there already! Try again")
            else:
                filled=False
        
        
        grid2[xturn] = turn
        currentGrid()
        ## Adding 1 to counter to count for a round
        counter=counter + 1
        ## Checking if its round 5
        if counter >= 5:
            gameOver=gameEnd(turn)
            if gameOver:
                break
        if counter == 9:
            print("THE GAME IS A TIE NO ONE WINS")
            break
        init()
        if turn=="x":
            turn="o"
        else:
            turn="x"

def gamemode():
    question=input("Would you like to play 2 players or fight against a pc? (pc/pvp)")
    if question=="pc":
        fillGridPc()
    else: 
        fillGrid()






filledSpot=[]

def randomNum():
    print(filledSpot)
    andomNum=random.randint(1,9)
    if andomNum not in filledSpot:
        return random.randint(1,9)
    else:
        randomNum()

def fillGridPc(): 
    turn="x"
    ##Setting round to 0
    init()
    currentGrid()
    counter=0
    for i in range(1,10):
        filled=True
        while filled:
            if turn=="x":
                xturn=int(input("Player " + turn + " where would you like to pick? (1-9)"))
            else:
                xturn=randomNum()
            if grid2[xturn] == "o" or grid2[xturn] == "x":
                print("Another player has put their x/o there already! Try again")
            else:
                filledSpot.append(xturn)
                filled=False
                time.sleep(1)
        
        
        grid2[xturn] = turn
        currentGrid()
        ## Adding 1 to counter to count for a round
        counter=counter + 1
        ## Checking if its round 5
        if counter >= 5:
            gameOver=gameEnd(turn)
            if gameOver:
                break
        if counter == 9:
            print("THE GAME IS A TIE NO ONE WINS")
            break
        init()
        if turn=="x":
            turn="o"
        else:
            turn="x"

## Checking if someone won the game by getting 3 in a row
def gameEnd(turn):
    if grid2[1] == grid2[2] == grid2[3] and grid2[1] != "#":
        print("PLAYER " + turn +  " WON THE GAME")
        return True
    if grid2[4] == grid2[5] == grid2[6] and grid2[4] != "#":
        print("PLAYER " + turn +  " WON THE GAME")
        return True
    if grid2[7] == grid2[8] == grid2[9] and grid2[7] != "#":
        print("PLAYER " + turn +  " WON THE GAME")
        return True
    if grid2[1] == grid2[4] == grid2[7] and grid2[1] != "#":
        print("PLAYER " + turn +  " WON THE GAME")
        return True
    if grid2[2] == grid2[5] == grid2[8] and grid2[2] != "#":
        print("PLAYER " + turn +  " WON THE GAME")
        return True
    if grid2[3] == grid2[6] == grid2[9] and grid2[3] != "#":
        print("PLAYER " + turn +  " WON THE GAME")
        return True
    if grid2[3] == grid2[5] == grid2[7] and grid2[3] != "#":
        print("PLAYER " + turn +  " WON THE GAME")
        return True
    if grid2[1] == grid2[5] == grid2[9] and grid2[1] != "#":
        print("PLAYER " + turn +  " WON THE GAME")
        return True
    return False

## Tic tac toe board cords
def init():
    print("Numbers on grid")
    print("1|2|3")
    print("4|5|6")
    print("7|8|9")


gamemode()