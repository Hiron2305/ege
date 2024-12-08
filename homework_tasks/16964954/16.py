for i in range(10000):
    res = 0
    for x in range(100000):
        if ((x&35 != 0 or x&22!=0) <= (x&15 == 0 <= x&i != 0)) == False:
            res = 1
    if res == 0:
        print(i)
        break