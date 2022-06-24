# Using python functions

# def search(element,list):
#     if element in list:
#         return list.index(element)
#     else:
#         return False


# Using no functions

# array=["bass","apples","Banana","Games","Human"]
# search=False
# element=input("What element are you trying to look for in array?")
# for i in range(len(array)):
#     if array[i] == element:
#         search = True
#         print(i)
#     elif i == len(array) -1 and search == False:
#         print("Error element not found")

def linearSearch(array):
    search=False
    element=int(input("What element are you trying to look for in array?"))
    for i in range(len(array)):
        if array[i] == element:
            search = True
            print(i)
            break
    if i == len(array) -1:
        print("Error element was not found")

def binarySearchAddon(array,searchElement):
    search=False
    for i in range(len(array)):
        if array[i] == searchElement:
            search = True
            print(i)
            break
    if i == len(array):
        print("Error element was not found")

def binarySearch(array):
    searchElement=int(input("What element are you trying to look for in array?"))
    mid=int(len(array) / 2)
    midElement=array[mid]
    if midElement == searchElement:
        print("Element found")
        print(mid+1)
    elif midElement < searchElement:
        print(binarySearchAddon(array[0:mid],searchElement))
        print("Element needs to be searched in the first half of the array")
    elif midElement > searchElement: 
        print(binarySearchAddon(array[mid:],searchElement))
        print("Element needs to be searched in the second half of the array")
    



array1=[1,2,5,8,9,6]
# print(linearSearch(array1))
binarySearch(array1)