values = []

values_zero = []
values_one = []
values_two = []


with open("27-B.txt") as file:
    num_value= int(file.readline())
    for i in range(num_value):
        current_num = int(file.readline())

        if (current_num % 3) == 0:
            values_zero.append(current_num)
        if (current_num % 3) == 1:
            values_one.append(current_num)
        if (current_num % 3) == 2:
            values_two.append(current_num)

values_zero.sort()
values_one.sort()
values_two.sort()
print(min(values_zero[0] + values_zero[1] + values_zero[2], values_one[0] + values_one[1] + values_one[2], values_two[0] + values_two[1] + values_two[2], values_zero[0] + values_one[0] + values_two[0]))
