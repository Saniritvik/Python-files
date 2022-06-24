

def addElements(value1,value2,value3=0):
    return value1 + value2 + value3

def multiplyElements(value1,value2,value3=1):
    return value1 * value2 * value3

def addElement(*args):
    sum=0
    for i in args:
        sum=sum+i
    return sum 

def main():
    print(addElements(1,2,3))
    # print(multiplyElements(2,3,4))
    print(addElement(1,2,3,4,5,6,7,8,9,10,11,12,13))
    square = lambda x:x**2
    print(square(2))
main()