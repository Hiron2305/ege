for x in range(0, 8):
    for y in range(0,8):
        a = x * (9 ** 4) + 0 * (9 ** 3) + 1 * (9 ** 2) + y * (9 ** 1) + 4 * (9 ** 0)
        b = x * (8 ** 4) + y * (8 ** 3) + 5 * (8 ** 2) + 4 * (8 ** 1) + 4 * (8 ** 0)

        if (a + b) % 89 == 0:
            print((a + b) // 89)