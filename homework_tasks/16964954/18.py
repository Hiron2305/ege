file = open("69927.txt")

a = [int(x) for x in file.read().split()]

counter = 0

max_sum = 0

counter_of_th = 0

for i in a:
    if i % 32 == 0:
        counter_of_th += 1

for i in range(len(a)- 1):
    first = a[i]
    second = a[i+1]

    if (first < 0 or second < 0) and (first + second < counter_of_th):
        counter += 1
        if first + second > max_sum:
            max_sum = first + second

print(counter)
print(max_sum)