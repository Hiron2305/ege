size = []

with open("27881.txt") as file:
    for i in range(4626):
        if i == 0:
            space_left = int(file.readline().strip().split()[0])
        else:
            line = file.readline().strip()
            size.append(int(line))

size.sort()
counter = 0
while space_left > 0:
    curr = size[counter]
    print(curr)
    if curr > space_left:
        print(counter, space_left, size[counter])
        break
    else:
        space_left -= size[counter]
        counter += 1

print(counter, space_left)
