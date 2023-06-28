import os
cwd = os.getcwd()
print(cwd)
os.chdir("../")
print(os.getcwd())