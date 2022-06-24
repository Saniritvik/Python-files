import random
num=random.randint(1,200)
question=0
tries=0
while question != num:
    question=int(input("Please try to guess this number"))
    tries+= 1
    if question > num:
        print("Go lower!")
    elif question < num:
        print("Go higher!")
    else:
        print("Congrats you have gotten the right answer! The amount tries it took you was "+ str(tries) + " tries")
