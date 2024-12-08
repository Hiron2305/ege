file = open('26.txt').readlines()
file =  sorted([list(map(int, i.split())) for i in file[1:]], key=lambda x: x[1])
answer = [file[0]]
for x in file[1:]:
    if x[0] > answer[-1][1] + 20:
        answer += [x]
file = list(filter(lambda x: x[0] > answer[-2][1] + 20, file))
print(len(answer), max(i[0] - answer[-2][1] for i in file))