questions="1-3;5;7;10-13"
questions2=questions.split(";")
result = 0
for i in questions2:
    if "-" in i:
        d = i.split("-")
        result += (int(d[1]) - int(d[0])+1)
    else:
        result+= 1
print(result)