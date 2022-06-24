word = input("Give me the suuper duper special word ")
known_word = ["-"] * len(word)
lives = 6
letter_history = []
i=lives
while i > 0:
    guess = input("Tell me what letter it might be? ")
    letter_history.append(guess)
    if guess in word: 
        print("You guessed a letter right!")
        for j in range(len(word)):
            if guess == word[j]:
                known_word[j] = guess
        print("number of lives left: ",i)
        print(known_word)
    else:
        i=i-1
        print("I am sorry but that was the wrong letter!")
        print("number of lives left: ",i)
        print(known_word)
    if "".join(known_word) == word:
        print("Congrats you did not kill the man!")
        break
if "".join(known_word) !=word:
    print("I am sorry you killed the man ")