numbers = []

with open("17_1.txt") as file:
    for i in range(10000):
        line = file.readline().strip()
        numbers.append(int(line))

min_21 = min([x for x in numbers if abs(x) % 21 == 0])

count = 0
max_sum = 0
for i in range(len(numbers) - 1):
    a, b = numbers[i], numbers[i + 1]
    if a % min_21 == 0 or b % min_21 == 0:
        count += 1
        max_sum = max(max_sum, (a + b))

print(count, max_sum)
