while True:
    print("1. Addition")
    print("2. Division")
    print("3. Subtraction")
    print("4. Multiplication")
    print("5. exit")
    operatio=input("What operation would you like to do?")
    num=int(input("How many numbers are in this eqaution?"))
    answer=0
    if operatio == "1":
        for i in range(num):
            temp=int(input("Enter a number"))
            answer+= temp
    elif operatio == "2":
        answer=1
        for i in range(num):
            temp=int(input("Enter a number"))
            answer/= temp
    elif operatio == "3":
        for i in range(num):
            temp=int(input("Enter a number"))
            answer-= temp
    elif operatio == "4":
        answer=1
        for i in range(num):
            temp=int(input("Enter a number"))
            answer*= temp
    elif operatio == "5":
        print("Thank for choosing the random python calculator")
        break
    else:
        print("This operation is invalid please try again")
    print(answer)