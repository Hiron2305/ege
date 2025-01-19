print('x y z w')
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                f = (z == (x <= w)) and ( x == (not(w <= y)))
                a = list([x, y, z, w])
                if f and a.count(0) >= 2:
                    print(x, y, z, w, '= 1')

                if (not(f)) and a.count(1) >= 1 and a.count(0) >= 1:
                    print(x,y,z,w, "= 0")