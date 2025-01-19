import itertools
from itertools import product, repeat

alph = "01a"
counter = 0
for i in product(alph, repeat=8):
    if i[0] != "0" and i.count('0') == 2 and i.count("a") <= 4:
        counter = counter + (5 ** i.count('a')) * (9 ** i.count('1'))

print(counter)