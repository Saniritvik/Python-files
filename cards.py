import random
class card: 
    suits=["hearts","spades","clubs","diamonds"]
    values=[None,None,"2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]
    def __init__(self,value,suit):
        self.value = value
        self.suit = suit
    
    def __lt__(self,c2):
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else: 
                return False
        return False
    
    def __gt__(self,c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else: 
                return False
        return False

class deck:
    def __init__(self):
        self.cards = []
        for i in range(2,15):
            for j in range(4):
                self.cards.append(card(i,j))
        random.shuffle(self.cards)
    
    def getCard(self):
        if len(self.cards) == 0:
            return
        else:
            return self.cards.pop()

class player:
    def __init__(self,name):
        self.name = name
        self.wins = 0
        self.card = None
        
class game:
    def __init__(self):
        n1 = input("P1 ENTER YOUR NAME NOW.")
        n2 = input("P2 ENTER YOUR NAME NOW.")
        self.p1 = player(n1)
        self.p2 = player(n2)
        self.deck = deck()
    
    def playGame(self):
        cards=self.deck.cards
        print("Beginning game")
        while len(cards) >= 2:
            response=input("WANNA QUIT? PRESS Q TO QUIT OR PRESS ANY KEY TO CONTINUE")
            if response == "Q":
                break
            p1card=self.deck.getCard()
            p2card=self.deck.getCard()
            print(self.p1.name + " pulled " + str(p1card.value) + " of " + card.suits[p1card.suit])
            print(self.p2.name + " pulled " + str(p2card.value) + " of " + card.suits[p2card.suit])
            if p1card > p2card:
                print(self.p1.name + " has won this round")
                self.p1.wins += 1
            elif p2card > p1card:
                print(self.p2.name + " has won this round")
                self.p2.wins += 1
            else:
                print("ITS A TIEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE :(")
        self.winner(self.p1,self.p2)
    
    def winner(self,p1,p2):
        if p1.wins > p2.wins: 
            print(self.p1.name + " has won")
        if p2.wins > p1.wins: 
            print(self.p2.name + " has won")
        if p2.wins == p1.wins:
            print("ITS A TIEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE :(")
            
g=game()
g.playGame()