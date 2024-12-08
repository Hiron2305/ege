values = [56789, 85758, 77700,50786]

for i in values:
    if i % 2 == 0:
        if (str(i)[0] in ['5','6','8'] and str(i)[0] != str(i)[-1]) and (str(i)[2] in ['5','7','9'] and str(i)[2] != str(i)[0]):
            print(values.index(i) + 1)