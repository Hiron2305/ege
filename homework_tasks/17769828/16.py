def f(x):
    if x < 3:
        return 1
    return f(x - 2)*(x - 1)

print(f(8))
