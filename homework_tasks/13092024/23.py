def act(x):
    if x == 10:
        return 1
    if x < 10:
        return 0
    return act(x - 1) + act(x - 10)

print(act(31))
