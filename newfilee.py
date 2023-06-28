import random
# st = str(input("Say something "))
# newst = ""
# print(st[0])
# print(st[-1])

# # for i in range(len(st) // 2):
# #     newst += st[i]
# # print(newst)

# fHalf = st[:len(st) //2]
# print(fHalf)
# sHalf = st[len(st) // 2:]
# print(sHalf)

# reverStr= st[::-1]
# print(reverStr)

# gameOver = False
# a = random.randint(1,100)

# while not gameOver:
#     ans = int(input("Guess the random number! "))

#     if ans > a: 
#         print("Try a lower number!")
    
#     elif ans < a : 
#         print("Try a higher number!")
    
#     else: 
#         print("Congrats you got the number!")
#         gameOver = True

# pal = input("Give me a word! ")
# splitted = pal.split(" ")
# joined = ""
# for i in range(len(splitted)):
#     joined += splitted[i]

# sliced = joined[::-1].lower()

# if sliced == joined.lower(): 
#     print("The word is the same backwards and forwards!")   
# else: 
#     print("Its just a word")

# e=[1,2,3,4,5,6,7,8,9,12084]
# even=[]

# for i in range(len(e)): 
#     if e[i] % 2 == 0: 
#        even.append(e[i])
# print(even)

# h = "supercalifragilisticexpialidocious"
# noVowl=""

# for i in range(len(h)): 
    
#     if h[i] not in "aeiou": 
#         noVowl += h[i]
# print(noVowl)

# f = ["Apple","Banana","Cherry","Grape","Blueberry","Orange","Pineapple","nope"]
# w = []
# count = 0
# winner=""
# ls = ""

# for i in range(len(f)):
#     if len(f[i]) >= 5: 
#         new.append(f[i])
# print(new)

# for i in range(len(f)):
#     if len(f[i]) > count:
#         count= len(f[i])
    
#     if len(f[i]) == count: 
#         winner = f[i]
# print(winner)

# for i in range(len(f)):
#     if len(f[i]) >= len(ls): 
#         ls = f[i]
# print(ls)

# for fruit in f: 
#     if len(fruit) >= 5:
#         new.append(fruit)
# print(new)

# for i in range(len(f)): 
#     if "a" in f[i] or "A" in f[i]: 
#         w.append(f[i])
# print(w)

# uno = [1,2,134,456,789,23789,45,5,6,7,8]
# dos = [1,2,80346,34568,46803,345689,8956,5,6,7,8]
# sum = 0

# # for i in range(len(uno)):
# #     if uno[i] in dos: 
# #         print(uno[i])

# for i in range(len(dos)):
#     if dos[i] % 2 != 0: 
#         sum += dos[i]
# print(sum)

# u = int(input("GIB NUMBER :) "))
# div=[]

# for i in range(1,u + 1):
#     if u % i == 0: 
#         div.append(i)
# print(div)

# b = [1,123,134,346,678,234,467,67234,7568,1234,467,124,567,123,67,123,45]
# a = []
# summer=0

# # for i in range(len(b)):
# #     if b[i] not in a: 
# #         a.append(b[i])
# # print(a)

# for i in range(len(b)):
#     if b[i] % 3 == 0 and b[i] % 5 == 0: 
#         summer+=b[i]

# print(summer)

# e = {
#     "Apple": 1,
#     "Blueberry":2,
#     "Banana":3,
#     "Pear":4
# }

# e.pop("Banana")
# print(e.values())
# print(e.keys())

# for key,value in e.items():
#     print(key,value)

# if "Apple" in e: 
#         print("Yay!")

# else:
#     print("Nope")

# if 3 in e.values(): 
#         print("Yay!")

# else:
#     print("Nope")

# print(e.items())

# uh = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
# count = {
    
# }

# for i in range(len(uh)): 
#     if uh[i] not in count:
#         count[uh[i]] = 1
#     else:
#         count[uh[i]] += 1
# print(count)

# d = {
#     "e":6,
#     "f":8,
#     "y":1
    
# }

# b = {
#     "u":6,
#     "i":1,
#     "f":14
# }

# for keys,values in d.items():
    
#     if keys in b.keys(): 
#         print("They got some things in common!")

#     else:
#         print("Awwww man its boring :(")


# sampleDict = {
#     "class": {        
#         "student": {            
#             "name": "Mike",            
#             "marks": {                
#                 "physics": 70,                
#                 "history": 80            
#                 }        
#             }    
#         }
#     }

# print(sampleDict["class"]["student"]["marks"]["history"])


e = {
    "Apple": 1,
    "Blueberry":2,
    "Banana":3,
    "Pear":4
}

e["Strawberry"] = e.pop("Apple")
print(e)