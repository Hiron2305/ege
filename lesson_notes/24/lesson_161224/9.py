lines = []
counter = 0

with open("9.txt") as file:
    for i in range(1000):
        a = file.readline()
        lines.append([int(x) for x in a.split()])


for i in lines:
    print(i)
    i.sort()
    print(i)

    f1 = i[0] * 6 < sum(i) - i[0]
    f2 = i[0] * i[-1] > i[1] * i[2]

    if f1 and f2:
        counter += 1
print(counter)