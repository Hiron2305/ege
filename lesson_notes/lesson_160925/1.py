a = int(input())

s = ""

while a > 0:
    s += str(a % 5)
    a //= 5

print(s[::-1])