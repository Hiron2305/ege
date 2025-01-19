values = []

results = []

with open("27-B.txt") as file:
    num_value= int(file.readline())
    for i in range(num_value):
        values.append(int(file.readline()))

for x in values:
    for y in values:
        if y != x:
            for z in values:
                print(x, y, z)
                if z != y and z != x:
                    if (x + y + z) % 3 == 0:
                        results.append(x + y + z)

print(min(results))
