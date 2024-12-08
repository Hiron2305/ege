from itertools import product


a = sorted("АЛГОРИТМ")

counter = 0

for i in product(a, repeat = 4):
    if "".join(i)[:2] == "ИГ":
        print(counter + 1, i)
    else:
        counter += 1
       # print("".join(i)[:1])