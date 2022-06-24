test=["2+2","1+2","P=NP","0+0"]
for i in test:
    if "+" in i:
        num=i.split("+")
        print(int(num[0])+int(num[1]))
    else:
        print("skipped")