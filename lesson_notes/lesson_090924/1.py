n = 44

while True:
    a = str(bin(n))[2:]

    sum_of_dig = sum(map(int, a[:-2]))

    if a[-2] == "1" and sum_of_dig % 2 == 1:
        break
    else:
        n += 1
print(n)