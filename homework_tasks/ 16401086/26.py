with open('26_demo.txt') as f:
    limit = int(f.readline().split()[0])
    values = sorted([int(line.strip()) for line in f])

total_sum = 0
count = 0
for val in values:
    if total_sum + val > limit:
        break
    total_sum += val
    count += 1

remaining = limit - total_sum
for val in values:
    if val - values[count - 1] <= remaining:
        result = val

print(count, result)
