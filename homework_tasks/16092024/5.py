n = 0
trigger = 0

while trigger < 100:
    to_bin = str(bin(n))[2:]
    to_bin += str(sum(map(int, to_bin)) % 2)
    to_bin += str(sum(map(int, to_bin)) % 2)

    trigger = int(to_bin, 2)
    n += 1
    print(trigger)

