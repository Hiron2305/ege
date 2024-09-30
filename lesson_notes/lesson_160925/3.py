a = "0123456789ABCDEFGH"

g = "AB9CH"

res = 0

counter = 0

for i in g[::-1]:
    value = a.index(i)
    res += value * (20 ** counter)
    counter += 1

print(res)