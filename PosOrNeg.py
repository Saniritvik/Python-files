a = [2, -7, 5, -64, -14,0]
neg=0
pos=0
for i in range(len(a)):
    if a[i] < 0:
        neg+=1
    else:
        pos+=1
print(neg)
print(pos)