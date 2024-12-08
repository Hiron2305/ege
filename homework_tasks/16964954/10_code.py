lines_result = 0

with open("10.txt") as file:
    for i in range(20000):
        line = file.readline()
        nums = [int(x) for x in line.split()]
        sum_of_three = 0
        sum_of_rest = 0
        counter_of_three = 0
        threes = []
        counter_of_rest = 0
        otheers = []
        for j in nums:
             if nums.count(j) == 3:
                 counter_of_three += 1
                 threes.append(j)
             elif nums.count(j) == 1:
                 counter_of_rest += 1
                 otheers.append(j)
        if counter_of_three == 3 and counter_of_rest == 3:
            for j in nums:
                if nums.count(j) == 3:
                    sum_of_three += j
                else:
                    sum_of_rest += j
        if sum_of_three ** 2 > sum_of_rest ** 2:
            lines_result+=1
print(lines_result)