input=["Skru op!","Skru op!","Skru op!","Skru op!","Skru op!","Skru ned!" ]
volume=7
for i in range(len(input)):
    if input[i] == "Skru op!":
        volume+= 1
    elif input[i] == "Skru ned!":
        volume-= 1
    if volume > 10:
        volume= 10
    elif volume < 0:
        volume= 0
print(volume)