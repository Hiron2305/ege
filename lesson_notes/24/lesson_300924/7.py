counter = 0

with open("099.txt") as file:
    for i in range(5000):
        a = file.readline()
        b = list(map(int, a.split()))
        x = b[0]
        y = b[1]
        z = b[2]

        if (x ** 2 == y**2 + z**2) or (y**2 == x**2 + z**2) or (z**2 == y**2 + x**2):
            counter += 1
print(counter)