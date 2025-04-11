file = open('17_9.txt')
numbers = [int(i) for i in file]


count = 0
max_diff = 0
for i in range(len(numbers) - 1):
    for j in range(i + 1, len(numbers)):
        a, b = numbers[i], numbers[j]
        if ((a - b) % 36 == 0) and (a % 13 == 0 or b % 13 == 0):
            count += 1
            max_diff = max(max_diff, (a - b), (b - a))

print(count, max_diff)
