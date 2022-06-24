num=5

#question 1
a=int(input("What is 2+2-2?"))
if a == 2:
    print("Oh wow you got it right!")
else:
    print("I am not gonna question... you wrong")
    num= num-1

#question 2
b=int(input("What 2 x 2 x 5 x 4 x 100 x 60 x 0"))
if b == 0:
    print("Congrats you know how to read! You got it right!")
else:
    print("Be more careful! It said 0 at the end! You are wrong")
    num= num-1

#question 3
c=int(input("(5 x 5) + (2 x 3)"))
if c==31:
    print("Nice! You know about PEMDAS instead of being on your phone!")
else:
    print("Nice! You were looking at your phone in class...")
    num= num-1

#question 4
d=int(input("How many sides does a triangle have?"))
if d==3:
    print("Nice! uhhh I don't know what else to say")
else:
    print("How did you mess this up?")
    num= num-1

#question 5
e=int(input("FINAL QUESTION: How many sides are on a sqaure"))
if e==4:
    print("Nice! You did not fail math or you did.")
else:
    print("You actually failed math (Maybe?).")
    num= num-1

#score
print(num)
if num==5:
    print("Wow! You actually passed... your not brain dead")
elif num==4:
    print("Nice job! Try better next time! Don't look at the phone.")
elif num==3:
    print("Okay man, listen up. Stop it. Ask your teacher for help.")
elif num==2:
    print("Are you okay? Did you read the questions wrong? Like huh?")
elif num==1:
    print("Your brain dead")
else:
    print("Wow.... GET A TUTOR ASAP")