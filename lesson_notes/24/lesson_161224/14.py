for x in range(13):
    for y in range(13):
        num1 = 8 * (13 ** 4) + x * (13 ** 3) + 7 * (13 ** 2) + 8 * (13) + y
        num2 = 7 * (18 ** 4) + 9 * (18 ** 3) + x * (18 ** 2) + y * (18) + 7

    if (num1 + num2) % 9 == 0:
        print((num1 + num2) // 9)
        break
