# this is a basic file program

#  file modes
# w -> for write
# a -> a for append
# r -> read
# + -> read and write

import os

# os.getcwd -> to get current working directory
print(os.getcwd())

# # this is to create a file variable or pointed in the specified mode
# f = open("test.txt", mode='r')

# # f.readline -> is to read data line by line
# data = f.readline()
# print(data, end="")

# # f.tell is to get the position of the file pointer
# print(f.tell())

# data = f.readline()
# print(data)

# print(f.tell())

# # f.seek is to change the location of file pointer
# f.seek(0)

# print(f.tell())

# # f.close is to close the file
# f.close()


# filePointer = open("input.txt", mode="r")
# fileData = filePointer.readlines()
# for line in fileData:
#     print(line, end="")


# fileWrite = open("test1.txt", "w+")

# fileWrite.writelines(["this is the line I want to write\n",
#                      "this is going to be second line"])

# print(fileWrite)

# fileWrite.writelines("this is the third line")

# data = fileWrite.read()

# print(data)

# fileWrite.close()

print("hello")
print(chr(27) + "[2J")
print("hello")
