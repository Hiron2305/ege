def f(x):
    if x == 0:
        return 0
    if x % 3 == 2:
        return f(x - 1) + 1
    return f(x // 3)

for i in range(1000):
    if f(i) == 6:
        print(i)
