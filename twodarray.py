## Init 2d array
twodArray = [["Bob", 5, "Math", "extra"], ["Joey", 6, "Science"],
             ["Bob1", 51, "Math1"], ["Joey1", 61, "Science1"]]




## Init 2d array
array=["Bob",5,"Math"]
array2=["Joey",6,"Science"]
twodArray=[array,array2]
print(twodArray)


## Printing collums and rows of a 2d array
print("Number of rows equal to " + str(len(twodArray)))
print("Number of collums equal to " + str(len(twodArray[0])))


## Accsesing the element at 0 row 0 collum
print(twodArray[0][0])
# print(twodArray[2][2])
print(twodArray[1][2])


## Updating at 0 collum 0 row 
twodArray[0][0] = "Jimmy"
print(twodArray)


## Printing all elements line by line
for i in range(0, len(twodArray)):
    for j in range(0, len(twodArray[i])):
        print(twodArray[i][j])


## Inserting new array
array3=["E","A","Sports"]
twodArray.insert(2,array3)
print(twodArray)


## Deleting last element using pop
print(twodArray.pop())
print(twodArray)


## Deleting first element del
del twodArray[0]
print(twodArray)