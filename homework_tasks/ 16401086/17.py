pairs = 0
max_sum = 0
with open('17.txt') as file:
    numbers = [int(x) for x in file]

for idx1 in range(len(numbers) - 1):
    for idx2 in range(idx1 + 1, len(numbers)):
        if (numbers[idx1] + numbers[idx2]) % 80 == 0 and (numbers[idx1] % 50 == 0 or numbers[idx2] % 50 == 0):
            pairs += 1
            max_sum = max(max_sum, numbers[idx1] + numbers[idx2])

print(pairs, max_sum)
