dict={

}
# dict.setdefault("A",10)
# print(dict)
name="Bob"
for i in name.lower():
    dict.setdefault(i,0)
    dict[i] = dict[i] + 1
print(dict)