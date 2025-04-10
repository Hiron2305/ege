s = open("24_5.txt")
s = s.read()

count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(1, len(s) - 1):
    if s[i - 1] == s[i + 1]:
        count[ord(s[i]) - 65] += 1

print(count)
