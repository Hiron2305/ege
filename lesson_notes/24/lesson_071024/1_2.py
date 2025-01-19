from itertools import *

for x in product("ABC", repeat = 2):
    print(x , "1")

for x in product("ABC", "DEB"):
    print(x)