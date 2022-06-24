n=10
num=3
steps=4
for i in range(steps):
    q=input("What cards have you chosen?")
    r=q.split(" ")
    if str(num) in r:
        print("Keep it")
    else:
        print("Remove it")