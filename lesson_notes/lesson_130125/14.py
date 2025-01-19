for x in range(12):
    for y in range(12):
        A = y * (12 ** 3) + 10 * (12 ** 2) + 10 * (12) + x
        B = x * (14 ** 3) + 0 + 2 * (14) + y
       # print((A + B) % 80)
        if (A + B) % 80 == 0:
            print(x, y, A + B // 80)