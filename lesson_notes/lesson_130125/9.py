counter = 0

with open('9.txt') as file:
    for i in range(5000):
        a = file.readline()
        numbers = [int(x) for x in a.split()]
        numbers.sort()
        if (numbers[0] + numbers[1]) < numbers[2] or numbers[0] + numbers[1] < numbers[3]:
            counter += 1

print(counter)