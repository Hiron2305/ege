from itertools import product, repeat

alph = ["К", "Л", "Р", "Т"]

result = []

for i in product(alph, repeat=4):
    result.append(i)

print(result[66])