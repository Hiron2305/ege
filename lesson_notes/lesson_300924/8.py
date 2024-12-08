counter = 0

with open("8.txt") as file:
    for i in range(5000):
        a = file.readline()
        b = list(map(int, a.split()))
        x = b[0] * b[1]
        y = b[1] * b[2]
        z = b[2] * b[0]

        if (x > y + z) or (y > x + z) or (z > y + x):
            counter += 1

print(5000 - counter)