from itertools import product, repeat

values = "012345678"

stack = []

for i in product(values, repeat = 5):
    if i[0] != "0" and int(i[0]) > int(i[1]) > int(i[2]) > int(i[3]) > int(i[4]):
        stack.append(i)

print(len(stack))
