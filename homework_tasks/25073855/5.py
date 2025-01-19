def triag(i):
    if i == 0:
        return "0"
    elif i == 1:
        return "1"
    elif i == 2:
        return "2"

    a = i // 3
    b = i % 3
    s = ""
    while a > 0:
        s += str(b)
        i = a
        a = i // 3
        b = i % 3

    return s[::-1] or "0"


r = 0
i = 1

while r < 220:
    a = triag(i)
    if i % 3 == 0:
        a += a[-2:]
    else:
        b = triag(sum([int(x) for x in a]))
        a += str(b)
    r = int(a, 3)
    print(r)
    i += 1
    print(i)