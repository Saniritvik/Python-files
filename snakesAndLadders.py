import random
# getting the player count

def players():
    numberOfPlayers = input("How many players will be playing?")
    return numberOfPlayers

# function to roll a dice

def dice(playerNumber):
    print("Rolling dice for ", playerNumber)
    return random.randint(1, 6)

# setting lader values

def ladders():
    ladders = {
        5: 19,
        8: 12,
        3: 65,
        14: 37,
        27: 51,
        33: 88
    }
    return ladders

# setting snake values

def snakes():
    snakes = {
        99: 87,
        15: 2,
        90: 70,
        94: 49,
        37: 12,
        80: 67
    }
    return snakes

# printing snakes

def whereSnake(snakesDictionary):

    for snake in snakesDictionary:
        print("Snake at position ",  snake,
              "will take you to position ", snakesDictionary[snake])

def whereLadder(laddersDictionary):

    for ladder in laddersDictionary:
        print("Ladder at position ",  ladder,
              "will take you to position ", laddersDictionary[ladder])

    return 1

def movePlayer(diceRoll, playerNo):
    print(playerNo, "played and rolled ", diceRoll)

def playerLocation(diceRoll, player, playerNumber):
    player += int(diceRoll)
    if player == 100:
        print("Player ", playerNumber,"WON THE GAMEEEEEEEEEEEEEEEEEE")
    if player > 100:
        player=player - diceRoll
        print("You would have won the game, but your roll was too high! Try again next turn!")
    if player in ladderz.keys():
        player = ladderz[player]
        print(
            "Player " + str(playerNumber) + "got a ladder and decided to go up becuase yes and is now at " + str(player))
    if player in snakez.keys():
        player = snakez[player]
        print(
            "UH OH! You have slide down a snake (For some reason) you are now at " + str(player))
    return player

def showPlayerLocation():
    print("Player 1 is at location:" + str(playerz_1))
    print("Player 2 is at location:" + str(playerz_2))

def antiCheat(rolled):
    if rolled > 6:
        print("Are you sure want to roll ", rolled)
        yn=input("(y/n)")
        yn=yn.upper()
        if yn == "Y" or yn == "N":
            if yn == "Y":
                print("Haha lol I will not move you cheater! Your turn has been skipped!")
                return 0
            else:
                diceRoll=int(input("Good.. You owned up to your mistakes mister or maam, here is your turn (Your rolling again)"))
                rolled=antiCheat(diceRoll)
                return rolled
        else:
            diceRoll=int(input("That was a mistake here is your turn back (Your rolling again)"))
            rolled=antiCheat(diceRoll)
            return rolled
    else:
        return rolled
        
ladderz = ladders()
snakez = snakes()
playerz_1 = 0
playerz_2 = 0

count =0
while(playerz_1 !=100 or playerz_2 !=100):
    if(count %2==0):
        print("********************")
        print("######LADDERS########")
        whereLadder(ladderz)
        print("#######SNAKES########")
        whereSnake(snakez)
        print("********************")
        print("Player 1 is playing")
        diceRoll =input("Roll the Dice:")
        diceRoll=antiCheat (int(diceRoll))
        playerz_1 =playerLocation(diceRoll, playerz_1, 1)
    else:
        print("Player 2 is playing")
        diceRoll =input("Roll the Dice:")
        diceRoll=antiCheat(int(diceRoll))
        playerz_2 =playerLocation(diceRoll, playerz_2, 2)
    showPlayerLocation()
    count = count+1
