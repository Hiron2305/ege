a = open('18_nums.txt').read().replace(",", ".").split("\n")

total_sum = -99999999999

for i in range(499):
    x = float(a[i])
    y = float(a[i+1])
   # print(x, y)
    current_sum = x

    while (abs(x - y) <= 8):
        current_sum += y
        print(current_sum)
        if current_sum > total_sum:
            total_sum = current_sum
        break

print(total_sum)