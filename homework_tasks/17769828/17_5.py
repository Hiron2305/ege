numbers_a = []
numbers_b = []

ca = 0
cb = 0

with open("17_5.txt") as file:
    for i in range(10000):
        line = file.readline().strip()
        if int(line) % 2 == 0:
            numbers_a.append(int(line))
            if int(line) % 31 == 0:
                ca = ca + 1
        else:
            numbers_b.append(int(line))
            if int(line) % 31 == 0:
                cb = cb + 1


print((ca * (ca - 1))//2 + (cb * (cb - 1))//2 + (ca * (len(numbers_a) - ca)) + (cb * (len(numbers_b) - cb)))
