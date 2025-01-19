from itertools import *

counter = 0
a = "0246"
b = "1347"

for i in permutations("0234567",5):
    s = "".join(i)
    for j in range(len(s) - 1):
        if s[j] in a and s[j+1] in a or s[j] in b and s[j + 1] in b:
            break
    else:
        if s[0] != "0":
            counter += 1

print(counter)