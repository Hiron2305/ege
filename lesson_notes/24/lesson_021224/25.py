import math
def find_val(num):

    dels = []

    for i in range(2, num//2):
        if num % i == 0:
            dels.append(i)
    if len(dels) >=5:
        a = 1
        for i in range(5):
            a *= dels[i]
        return a
    else:
        return 0






counter = 0
answer = []
start = 500000000
while counter < 5:
    if 0 < find_val(start) < start:
        counter += 1
        answer.append(start)

    start += 1

print(sorted(answer))
