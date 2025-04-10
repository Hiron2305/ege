print("x y z w u")

for x in 0,1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                for u in 0, 1:
                    F = ((z <= w) and (y != x)) <= (u == (y or z))
                    if F == 0:
                        print(x, y, z, w, u)
