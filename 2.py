def act(n, a):
    left = n % 3
    to_bin = bin(left)[2:]

    if left != 2:
        a += str(0) + str(to_bin)
    else:
        a += str(to_bin)
    return a



def act2(n, a):
    left = n % 5
    to_bin = bin(left)[2:]

    if left != 4 and left != 0:
        a += str(0) + str(to_bin)
    elif left == 0:
        a += str(0) + str(0) + str(to_bin)
    else:
        a += str(to_bin)

    return a


count = 0
for n in range(1222222222, 1555555666):
    a = str(bin(n))[2:]

    a = act(n, a)

    n = int(a, 2)

    a = act2(n, a)

    n = int(a, 2)

