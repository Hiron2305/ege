def triag(n):
    res = ''
    while n > 0:
        res =  str(n % 3) + res
        n //= 3
    return res

n = 1
trigger = 0

while trigger < 150:
    a = str(triag(n))
    if n % 3 == 0:
        a = a + str(a)[-3:]
        trigger = int(a, 3)
    else:
        res = (n % 3) * 3
        res2 = triag(res)
        a = a + str(res2)
        trigger = int(a, 3)
    n += 1
else:
    print(n - 1)