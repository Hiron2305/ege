sequence = open('24.txt').read().strip().replace('A', '*').replace('B', '*').replace('C', '*')
longest = current = 1

for idx in range(1, len(sequence)):
    if sequence[idx-1] + sequence[idx] != '**':
        current += 1
        longest = max(longest, current)
    else:
        current = 1
print(longest)
