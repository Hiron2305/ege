counter = 0
start_point = 0
flag = True
i = 1

while flag:
    n = str(bin(i))[2:]
    dividor = i % 4
    n += str(bin(dividor))[2:]
    r = int(n, 2)
    if start_point == 0:
        start_point = r
    else:
        if r < start_point + 65:
            counter += 1
        else:
            flag = False
    i += 1
    #print(i)
    #print(r)

print(counter)