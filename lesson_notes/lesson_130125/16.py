from functools import *
from  sys import *
setrecursionlimit(10000)

counter = 0

@lru_cache(None)
def F(n):
    if n < 10:
        return n
    if n >= 10:
        return F(n % 10) + F(n // 10)

for n in range(2 ** 63):
    if F(n) == 159:
        counter += 1
print(counter)