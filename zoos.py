zoo = input()
z, o = 0, 0
for i in zoo:
    if i == "z":
        z+=1
    else:
        o+=1
print("Yes") if 2*z == o else print("No")
