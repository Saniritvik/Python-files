array=[1,3,7,6,8,9]
half1=array[0:4]
half2=array[4:6]
reverse=array[::-1]
arrray=[]
for i in range(len(array)-1,-1,-1):
    arrray.append(array[i])
print(arrray)
print(reverse)
print(half2[::-1])