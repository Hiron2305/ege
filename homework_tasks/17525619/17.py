numbers = []

with open("17_2.txt") as file:
    for i in range(6634):
        line = file.readline().strip()
        numbers.append(int(line))

max_13 = max([x for x in numbers if abs(x) % 100 == 13])

count = 0
max_sum = 0
for i in range(len(numbers) - 2):
    a, b, c = numbers[i], numbers[i + 1], numbers[i + 2]
    lens = [1 for j in (a,b,c) if len(str(j)) == 3]
    if (a + b + c) < max_13 and len(lens) == 2:
        count += 1
        max_sum = max(max_sum, (a + b + c))

print(count, max_sum)
