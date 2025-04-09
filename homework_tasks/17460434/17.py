numbers = []

with open("17_1.txt") as file:
    for i in range(10000):
        line = file.readline().strip()
        numbers.append(int(line))

min_5 = min([x for x in numbers if abs(x) % 10 == 5 and 99 < x < 1000])

count = 0
min_sum = 10000000
for i in range(len(numbers) - 1):
    a, b = numbers[i], numbers[i + 1]
    if (a + b) % min_5 == 0 and (((99 < a < 1000) and (b < 100 or b > 999)) or ((99 < b < 1000) and (a < 100 or a > 999))):
        count += 1
        min_sum = min(min_sum, (a + b))

print(count, min_sum)
