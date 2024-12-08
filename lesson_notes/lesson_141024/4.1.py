from itertools import product

a = sorted("АБЗИ")

counter = 0

for i in product(a, repeat=4):
    if "".join(i) != "ИЗБА":
        counter += 1
    else:
        print(counter + 1, i)