from itertools import product

def check(i):
    flag = True
    for k, l in enumerate(i[:-1]):
        print(l, k)
        if k != 0:
            if l == "Я" and (i[k-1] == "Я" or i[k+1] == "Я"):
                flag = False
        else:
            if l == "Я" and i[k+1] == "Я":
                flag = False
    return flag


alph = "Я Н В А Р Ь".split()
alph.sort()
print(alph)
counter = 1
result = 0
for i in product(alph, repeat = 5):
    print(i, counter)
    if i[0] != "Я" and i.count("Ь") <= 1 and check(i):
        result = counter
        counter += 1
    else:
        counter += 1
print(result)

