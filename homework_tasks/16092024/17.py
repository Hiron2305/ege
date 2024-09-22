with open('17.txt') as f:
    numbers = list(map(int, f.readlines()))

count_pairs = 0
max_sum = 0

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        pair_sum = numbers[i] + numbers[j]
        if pair_sum % 120 == 0:
            count_pairs += 1
            if pair_sum > max_sum:
                max_sum = pair_sum

print(count_pairs)
print(max_sum)
