r = 0
n = 1
while r < 123456789:
    b = str(bin(n))[2:]
    for i in range(3):
        if sum([int(x) for x in b]) % 2 == 1:
            b += "1"
        else:
            b += "0"

    r = int(b, 2)
    n += 1
else:
    print("r:", r, "n:", n)