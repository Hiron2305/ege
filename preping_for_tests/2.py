from itertools import product, repeat

a = "АОУ"
counter = 0
for i in product(a, repeat=5):
    if counter == 209:
        print(i)
        break
    else:
        counter += 1
