def first_eq(x):
    return 2 * 13**4 + 6 * 13**3 + x * 13**2 + 9 * 13 + 8

def second_eq(x):
    return 4 * 13**4 + x * 13**3 + 2 * 13**2 + 9 * 13 + 6

for x in range(13):
    first = first_eq(x)
    second = second_eq(x)

    if (first + second) % 34 == 0:
        print((first + second) // 34)
        break