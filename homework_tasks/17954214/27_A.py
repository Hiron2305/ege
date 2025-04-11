nums_a, nums_b, nums_c = [], [], []

with open("27-A_8.txt") as file:
    n = int(file.readline())
    for i in range(n):
        line = int(file.readline())
        if line % 3 == 0:
            nums_a.append(line)
        elif line % 3 == 1:
            nums_b.append(line)
        else:
            nums_c.append(line)

nums_a.sort()
nums_b.sort()
nums_c.sort()

sums = [nums_a[0] + nums_a[1] + nums_a[2], nums_b[0] + nums_b[1] + nums_b[2], nums_c[0] + nums_c[1] + nums_c[2], nums_a[0] + nums_b[0] + nums_c[0]]

print(min(sums))
