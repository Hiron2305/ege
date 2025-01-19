def process_number(n):
    digits = [int(d) for d in str(n)]
    sums = [digits[0] + digits[1], digits[1] + digits[2], digits[2] + digits[3]]
    sums.remove(min(sums))
    return int("".join(map(str, sorted(sums))))

target_result = 1215
for num in range(1000, 10000):
    if process_number(num) == target_result:
        print(num)
        break
