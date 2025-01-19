values = [579, 878, 770,576]

for i in [5,6,8]:
    for j in [5,7,9]:
        for k in [0,6,8]:
            if (i != k and j != i):
                if (100*i + 10*j + k) in values:
                    print(values.index(100*i + 10*j + k) + 1)