from itertools import product, repeat

a = sorted("КОМПЬТЕР")

s = []

for i in product(a, repeat = 5):
    s.append(i)


s2 = [x for x in s if x.count("К") == 0 and x.count("Р") == 2]
print(s.index(s2[-1]) + 1, s2[-1])