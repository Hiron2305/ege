def f(x):
    if x < 3:
        return 1
    if x % 2 == 1:
        return f(x - 1) + 3 * f(x - 2)

    s = 0
    for i in range(1, x):
        s += f(i)
    return s

print(f(28))
