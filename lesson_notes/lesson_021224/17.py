count, m = 0, 0
f = open('17.txt')
l = [int(i) for i in f]
for i in range(len(l) - 1):
    for j in range(i + 1, len(l)):
        if (l[i] + l[j]) % 2 != 0 and (l[i] * l[j]) % 5 == 0:
            count += 1
            m = max(m, l[i] + l[j])
print(count, m)