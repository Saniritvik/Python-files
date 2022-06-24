#rot 13 decphyer
secret_word="HELLO"
answer=""
for i in range(len(secret_word)):
    num=ord(secret_word[i])
    if num > ord("M"):
        answer+=chr(num-13)
    else:
        answer+=chr(num+13)
print(answer)