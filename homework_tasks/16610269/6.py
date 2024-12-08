n = 1009
res = 0

while res != 2018:
    a = str(bin(n))[2:-1]
    #print(a)

    if n % 2 == 1:
        a += "10"
    else:
        a += "01"
    res = int(a, 2)
    n += 1
    print(n)
    print(res)