# Largest element
array=[1,6,3,4,5]
number=0
for i in range(len(array)):
    if number < array[i]:
        number = array[i]
print("The greatest number is "+ str(number))

# Bubble sort
for j in range(len(array)):
    for i in range(len(array)-1):
        if array[i] > array[i+1]:
            array[i],array[i+1] = array[i+1],array[i]