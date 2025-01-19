def check(x):
    if ((len(str(x)) == 5 and str(x)[0] != "-") or (len(str(x)) == 6 and str(x)[0] == "-")) and str(x)[-2:] == "43":
        return True



with open("17_19249.txt") as file:
    a = [int(x) for x in file.read().split()]


max_avaliable = -9999999999
for i in a:
    if check(i) and i > max_avaliable:
        max_avaliable = i

print(max_avaliable)

counter = 0
min_s = float('inf')
for i in range(1, len(a) - 1):
    first = a[i-1]
    second = a[i]
    third = a[i+1]
    s = first ** 2 + second ** 2 + third ** 2
    if (check(first) or check(second) or check(third)) and s <= max_avaliable ** 2 :
        counter += 1
        if check(first):
            print(first)
        if check(second):
            print(second)
        if check(third):
            print(third)
        if s < min_s:
            min_s = s
print(counter, min_s)