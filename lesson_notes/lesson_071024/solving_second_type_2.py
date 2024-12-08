from itertools import *

def f1(x, y, z, w):
    return ((w == x) and (y <= z))


def f2(x,y,z,w):
    return ((w <= x) <= (y == z))

for a1, a2, a3, a4 in product([0, 1], repeat=4):
    tab = [(1, a1, 1, 1), (a2, 1, 0, 0), (a3, 0, 0, a4)]
    print(tab, len(tab), len(set(tab)))
    if len(tab) == len(set(tab)):
        for p in permutations('xyzw'):
            if ([f1(**dict(zip(p, r))) for r in tab] == [1, 1, 0] and (([f2(**dict(zip(p, r))) for r in tab] == [0, 0, 0] or ([f2(**dict(zip(p, r))) for r in tab] == [0, 1, 0])))):
                print(p)