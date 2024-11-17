tar = 0
n = 0
while tar < 102:
    b = str(bin(n))[2:]
    if n % 2 == 0:
        b += "10"
    else: b += "01"
    tar = int(b, 2)
    print(tar)
    n += 1