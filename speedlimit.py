distance=0
pairs=int(input("How many pairs?"))
prev=0
for i in range(pairs):
    speed=int(input("What is the speed?"))
    hours=int(input("How many hours?"))
    distance+= (speed * (hours - prev))
    prev=hours
print(distance)

