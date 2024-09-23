counter = 0
for number in range(1000, 10000):
    digits = list(map(int, str(number)))
    if all(digit % 2 != 0 for digit in digits):
        sum1, sum2 = digits[0] + digits[1], digits[2] + digits[3]
        combined = str(min(sum1, sum2)) + str(max(sum1, sum2))
        if combined == '616':
            counter += 1
print(counter)
