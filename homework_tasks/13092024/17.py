numbers = []

with open("17.txt") as file:
    for i in range(5000):
        line = file.readline().strip()
        numbers.append(int(line))

print(numbers)

min_5 = min([x for x in numbers if abs(x) % 10 == 5])

count = 0
max_sum_of_squares = float('-inf')
for i in range(len(numbers) - 1):
    a, b = numbers[i], numbers[i + 1]
    if abs(a) % 10 == 5 and abs(b) % 10 != 5:
        lesser = a
    elif abs(b) % 10 == 5 and abs(a) % 10 != 5:
        lesser = b
    else:
        continue

    sum_of_squares = a**2 + b**2
    if sum_of_squares < min_5**2:
        count += 1
        max_sum_of_squares = max(max_sum_of_squares, sum_of_squares)

print(count, max_sum_of_squares)
