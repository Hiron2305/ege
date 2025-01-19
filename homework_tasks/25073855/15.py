for a in range(100):
    counter = 0
    for x in range(1, 501):
        for y in range(1, 501):
            f = ((x - (3 * y)) < a) or (y > 400) or (x > 56)
            if f == 0:
                break
            if f == 1:
                counter += 1
            if counter == 250000:
                print(a)
