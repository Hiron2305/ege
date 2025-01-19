result = 0

with open("9.txt") as file:
    for i in range(18000):
        a = [int(x) for x in file.readline().split()]

        counter_list = []

        for j in a:
            counter_list.append(a.count(j))


