print("x y z w")

for x in 0,1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = (x and y) or (y == z) or w
                if F == 0:
                    print(x, y, z, w)
