from itertools import product

alph = ["В", "Е", "Р", "О", "Н", "И", "К", "А"]

res = []


counter = 0
for i in product(alph, repeat = 3):
    if i.count("В") == 1:
        counter += 1
        if i.count("А") == 0:
            print(i, counter)
