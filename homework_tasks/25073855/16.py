from functools import *
import sys
sys.setrecursionlimit(100000000)

counter = 0

@lru_cache(None)
def F(n):
    if n < 5:
        return n
    if n >= 5:
        return 2 * n * F(n - 4)

print((F(13766) - (9 * F(13762))) / F(13758))