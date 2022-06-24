a = [70, 11, 20, 4, 100, 100]
# print(max(a))
greatest=a[0]
greatest2=a[0]
for i in range(len(a)):
    if greatest < a[i]:
        greatest=a[i]

for j in range(len(a)):
    if greatest2 < a[j] and a[j] != greatest:
        greatest2=a[j]
print(greatest)
print(greatest2)