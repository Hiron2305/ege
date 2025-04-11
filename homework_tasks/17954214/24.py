s = open("24_8.txt")
s = s.read()

count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(1, len(s) - 1):
    if s[i - 1] == 'E':
        count[ord(s[i]) - 65] += 1

print(count)
