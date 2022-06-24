a="ATCCGCTTAGAGGGATT"
b="GTCCGTTTAGAAGGTTT"
a="abcdefghijklmnopqrstuvwxyz"
b="bcdefghijklmnopqrstuvwxyza"
answer=""
for i in range(len(a)):
    if a[i] == b[i]:
        answer+="."
    else:
        answer+="*"
print(answer)
