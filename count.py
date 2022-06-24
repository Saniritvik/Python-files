a = [15, 6, 7, 10, 12, 20, 10, 28, 10]
x = 10
b=0
for i in range(len(a)):
    if a[i]== x:
        b+=1
print(str(x) + " Occured " + str(b) + " times")
print(a.count(x))