f = open("27-B.txt")
lines = f.readlines()
n = int(lines[0])

total, second_sum, third_sum = 0, 0, 0
minimum_difference = 20001

for i in range(1, n + 1):
    a, b, c = map(int, lines[i].split())
    min_val = min(a, b, c)
    total += min_val
    if min_val == a:
        second_sum += min(b, c)
        third_sum += max(b, c)
        if abs(a - b) % 2 != 0:
            minimum_difference = min(minimum_difference, abs(a - b))
        elif abs(a - c) % 2 != 0:
            minimum_difference = min(minimum_difference, abs(a - c))
    elif min_val == b:
        second_sum += min(a, c)
        third_sum += max(a, c)
        if abs(b - a) % 2 != 0:
            minimum_difference = min(minimum_difference, abs(b - a))
        elif abs(b - c) % 2 != 0:
            minimum_difference = min(minimum_difference, abs(b - c))
    else:
        second_sum += min(a, b)
        third_sum += max(a, b)
        if abs(c - a) % 2 != 0:
            minimum_difference = min(minimum_difference, abs(c - a))
        elif abs(c - b) % 2 != 0:
            minimum_difference = min(minimum_difference, abs(c - b))

if (second_sum + third_sum) % 2 != 0:
    print(total)
else:
    print(total + minimum_difference)
