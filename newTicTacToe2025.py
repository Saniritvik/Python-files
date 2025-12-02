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
        
    for i in range(1,10): 
        turn_player = input("Place your marker on the board(1-9)")
        filled = True



tic_tac_toe()
