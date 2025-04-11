n = 0
trigger = 0

while trigger < 103:
    to_bin = str(bin(n))[2:]
    to_bin += to_bin[-1]
    to_bin += str((int(to_bin[-1]) + 1) % 2)
    trigger = int(to_bin, 2)
    n += 1

print(trigger)
