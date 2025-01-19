print("x y z w")
for x in 0,1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                f = ((x == y) <= (not(z) or w)) == (not((w <= x) or (y <= z)))
                if f:
                    print(x, y, z, w)
