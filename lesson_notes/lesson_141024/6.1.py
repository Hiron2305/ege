from itertools import product

from scipy.constants import value

a = sorted("МАНГУСТ")

s = []
s1 = []

for i in product(a, repeat = 6):
    value = "".join(i)

    s.append(i)

    if value[0] != "У" and value.count("М") == 2 and value.count("Г") <= 1:
        s1.append(i)

print(s.index(s1[-1]) + 1)
