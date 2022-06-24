

##Int 2d array for tic tac toe
grid=[["#","#","#"],["#","#","#"],["#","#","#"]]

## Printing the current grid
def currentGrid():
    for i in range(0,len(grid)):
        print(grid[i])

## Cords for the player to write
def init():
    print("2d array cords (row,collum)")
    print("(0,0),(0,1),(0,2)")
    print("(1,0),(1,1),(1,2)")
    print("(2,0),(2,1),(2,2)")

def fillGrid(): 
    turn="x"
    ##Setting round to 0
    counter=0
    for i in range(1,10):
        filled=True
        while filled:
            row=int(input("Player " + turn + " which row would you like to pick? (0-2)"))
            collum=int(input("Player " + turn + " which collum would you like to pick? (0-2)"))
            if grid[row][collum] == "o" or grid[row][collum] == "x":
                print("Another player has put their x/o there already! Try again")
            else:
                filled=False
        
        
        grid[row][collum] = turn
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

def gameEnd(turn):
    ## Straight line
    if grid[0][0] == grid[0][1] == grid[0][2] and grid[0][0] != "#":
        print("PLAYER " + turn +  " WON THE GAME")
        return True
    if grid[1][0] == grid[1][1] == grid[1][2] and grid[1][0] != "#":
        print("PLAYER " + turn +  " WON THE GAME")
        return True
    if grid[2][0] == grid[2][1] == grid[2][2] and grid[2][0] != "#":
        print("PLAYER " + turn +  " WON THE GAME")
        return True
    ## Up and down
    if grid[0][0] == grid[1][0] == grid[2][0] and grid[0][0] != "#":
        print("PLAYER " + turn +  " WON THE GAME")
        return True
    if grid[0][1] == grid[1][1] == grid[2][1] and grid[0][1] != "#":
        print("PLAYER " + turn +  " WON THE GAME")
        return True
    if grid[0][2] == grid[1][2] == grid[2][2] and grid[0][2] != "#":
        print("PLAYER " + turn +  " WON THE GAME")
        return True
    ##Diagonal   
    if grid[0][0] == grid[1][1] == grid[2][2] and grid[0][0] != "#":
        print("PLAYER " + turn +  " WON THE GAME")
        return True
    if grid[2][0] == grid[1][1] == grid[0][2] and grid[2][0] != "#":
        print("PLAYER " + turn +  " WON THE GAME")
        return True
    return False

currentGrid()
init()
fillGrid()