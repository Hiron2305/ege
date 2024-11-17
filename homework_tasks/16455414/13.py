l = "8" * 99 + "1"

a = "133"
b = "881"

while a in l or b in l:
    if a in l:
        l = l.replace("133", "81", 1)
    else:
        l = l.replace("881", "13", 1)



print(l)

