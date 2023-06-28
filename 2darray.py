import numpy as np
# a = [[1,2,3,4,5], [8345,82455,80234,90234,234890], [123478,235978,3845,2431,23894]]

# for i in range(len(a)): 
#     for j in range(len(a[0])):
#         print(i,j,a[i][j])

# board = np.zeros((6,7))

# colSize = 7
# rowSize= 6
# chip = 0

# for c in range(colSize-3):
#     for r in range(rowSize):
#         print("col",c, "row", r)
#         if board[r,c] == chip and board[r,c+1] == chip and board[r,c+2] == chip and board[r,c+3] == chip:
#             print("Boy")

# day 1 is equal to 11,12,13,14 
# day 2 is equal to 15,16,17,18
# day 3 is equal to 19,20,21,22
# day 4 is equal to 23,24,25,26
d1 = [11,12,13,14]
d2 = [15,16,17,18]
d3 = [19,20,21,22]
d4 = [23,24,25,26]
d5 = [27,28,29,30]
t = [[11,12,13,14],
     [15,16,17,18],
     [19,20,21,22],
     [23,24,25,26]]

# t.insert(1,d5)
# print(t)
# t[2][2] = 13
# print(t)
# t[3] = [1,2,3,4]
# print(t)
# del t[3]
# print(t)
sum = 0
for i in range(len(t)): 
    sum += t[i][i]
print(sum)