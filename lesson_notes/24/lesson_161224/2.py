print("x y z w")
both_list = []
first_list = []
second_list = []


for x in 0,1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                f1 = (x or not(y)) <= (w == z)
                f2 = (x or not(y)) == (w <= z)

                if f1 == 0 == f2:
                    both_list.append([x, y, z, w])

                if f1 == 0:
                    first_list.append([x, y, z, w])

                if f2 == 0:
                    second_list.append([x, y, z, w])


print("BOTH")
for i in both_list:
    print(i)

print("FIRST")
for i in first_list:
    print(i)

print("SECOND")
for i in second_list:
    print(i)
