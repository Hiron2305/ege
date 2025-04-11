print("x y z w")

for x in 0,1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = ((z <= w) or (y == w)) and ((x or z) == y)
                if F == 1:
                    print(x, y, z, w)
