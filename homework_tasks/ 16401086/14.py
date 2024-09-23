num = 9**8 + 3**5 - 9
ternary = ''
while num:
    ternary = str(num % 3) + ternary
    num //= 3
print(ternary.count('2'))
