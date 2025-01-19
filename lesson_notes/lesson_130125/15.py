counter = 0

for A in range(100):
    for x in range(100):
        for y in range(100):
            f = ((x < 6) <= (x * x < A)) and ((y * y <= A) <= (y <= 6))
            if f:
                counter += 1
            else:
                break
        else:
            break
    else:
        break

print(counter)