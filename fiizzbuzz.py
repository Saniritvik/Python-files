n=70
l=[]
for i in range(1,n+1):
    if i % 7 ==0 and i % 3==0 and i % 5 ==0:
        l.append("FizzBuzzJazz")
    elif i % 3 ==0 and i % 5 ==0:
        l.append("FizzBuzz")
    elif i % 7==0 and i % 3==0:
        l.append("FizzJazz")
    elif i % 7 ==0 and i % 5 ==0:
        l.append("BuzzJazz")
    elif i % 3 ==0: 
        l.append("Fizz")
    elif i % 5 ==0:
        l.append("Buzz")
    elif i % 7 ==0:
        l.append("Jazz")
    else:
        l.append(i)    
print(l)