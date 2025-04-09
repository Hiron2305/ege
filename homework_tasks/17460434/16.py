def f(x):
    if x == 0:
        return 0
    if x > 0 and x % 3 == 0:
        return f(x//3)
    else:
        return (x%3) + f(x-(x%3))

for i in range(500):
    if f(i) == 11:
        print(i)
