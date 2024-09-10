def act(num):
    x = sum(map(int, str(num))) % 2
    num += str(x)
    x = sum(map(int, str(num))) % 2
    num += str(x)
    return int(num, 2)

trigger = 0
n = 1
while trigger < 43 :
    b = str(bin(n))[2:]
    print(b)
    trigger = act(b)
    n += 1
else:
    print(trigger)