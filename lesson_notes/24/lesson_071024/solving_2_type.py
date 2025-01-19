from itertools import *

def f(x, y, z):
    return ((x or y) <= (z == x))


for a1, a2, a3 in product([0, 1], repeat=3):
    tab = [(a1,0, 0), (a2, 0, a3)]
    print(tab, len(tab), len(set(tab)))
    if len(tab) == len(set(tab)):
        for p in permutations('xyz'):
            if [f(**dict(zip(p, r))) for r in tab] == [0, 0]:
                print(p)