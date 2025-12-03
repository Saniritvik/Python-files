import random 
import time 

def tic_tac_toe(): 
    grid_dict = {
        1: "#",
        2: "#",
        3: "#",
        4: "#",
        5: "#",
        6: "#",
        7: "#",
        8: "#",
        9: "#"
    }
    filled = []
        
    print("Numbers on grid")
    print("1|2|3")
    print("4|5|6")
    print("7|8|9")
    
    print("Current grid")
    print(grid_dict[1] + "|" + grid_dict[2] + "|" + grid_dict[3])
    print(grid_dict[4] + "|" + grid_dict[5] + "|" + grid_dict[6])
    print(grid_dict[7] + "|" + grid_dict[8] + "|" + grid_dict[9])
    
    turn = "player"
    for i in range(1,10): 
        filled = True
        while filled: 
            turn_player = int(input("Place your marker on the board(1-9)"))
            if grid_dict[turn_player] == "o" or grid_dict[turn_player] == "x":
                print("This space is already occupied please try another value")
            else: 
                filled = False
        

        

        




tic_tac_toe()
