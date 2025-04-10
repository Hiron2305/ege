odd_nums = []
even_nums = []

with open("26_7.txt") as file:
    for i in range(5001):
        number = int(file.readline())
        if number % 2 == 0:
            even_nums.append(number)
        else:
            odd_nums.append(number)

counter = 0
max_sum = 0

for i in odd_nums:
    for j in even_nums:
        if (i + j) in odd_nums:
            max_sum = max(max_sum, i + j)
            counter += 1


print(counter, max_sum)
