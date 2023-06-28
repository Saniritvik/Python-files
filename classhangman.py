import random

#"bar","slide","boy","wings","chicken","winter","apple","blue","bed","chair","mouse","keyboard","monitor"

words=["chicken wing"]
movie=["infinity war","toy story","spiderman far from home","batman","tom and jerry"]
food=["chicken wing","turkey","cookies","gingerbread","rice","potatos","banana","cheese","apple"]
school=["pencil","notebook","teacher","math","science","english","social studies","spanish","french","turkish"]
cartoons=["mickey mouse","the grinch","star wars","sonic prime","the owl house"]
characters=["mickey mouse","donald duck","spiderman","batman","superman",]
jobs=["software developer","architect","teacher","scientist","milltary general","guard"]

catergory=input("What category do you wanna play? (words,movie,food,school,cartoons,characters,jobs)")

if catergory == "words": 
    wordToGuess=random.choice(words)
if catergory == "movie":
    wordToGuess=random.choice(movie)
if catergory == "food":
    wordToGuess=random.choice(food)
if catergory == "school":
    wordToGuess=random.choice(school)
if catergory == "cartoons":
    wordToGuess=random.choice(cartoons)
if catergory == "characters":
    wordToGuess=random.choice(characters)
if catergory == "jobs":
    wordToGuess=random.choice(jobs)

man=["___","| 0","|\|/","| |","|/\\"]

class HangMan:
    def __init__(self,word):
        self.word = word
        self.wrong = 0
        self.answer = list("_" * len(self.word))
        self.guessed = []
        
    def getUi(self):
        userin=input("Type a letter ")
        return userin
    
    def invalid(self,userin):
        return userin.isdigit() or (userin.isalpha() and len(userin) > 1) or (userin in self.guessed)
    
    def findIndex(self,userinn):
        indexWords=[]
        for i,char in enumerate(self.word):
            if char == userinn:
                indexWords.append(i)
        return indexWords
    
    def updateAns(self,userinn,indexes):
        for i in indexes:
            self.answer[i] = userinn
            
    def gameStatus(self):
        print("\n".join(man[0:self.wrong]))
        print("".join(self.answer))
    
    def play(self):
        while self.wrong < len(man):
            self.gameStatus()
            userinn = self.getUi()
            
            if self.invalid(userinn):
               print("Input is INVALID TYPE IT AGAIN!!!!!")
               continue
            
            if userinn in self.answer:
               print("ALREADY GUESSED IT LEARN HOW TO READ!!")
               continue
            
            if userinn in self.word: 
                indexes= self.findIndex(userinn)
                self.updateAns(userinn,indexes)
                
                if self.answer.count("_") == self.word.count(" "):
                    print("YOU DID NOT HANG A MAN! :D")
                    print(self.word)
                    quit()
            else:
                self.wrong = self.wrong + 1
            self.guessed.append(userinn)
        print("YOU HANGED A MAN >:(")
        print("The correct word was " + self.word)
        print(self.gameStatus())


hangman=HangMan(wordToGuess)
hangman.play()