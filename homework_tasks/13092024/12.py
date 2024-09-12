def transform(s):
    while '01' in s or '02' in s or '03' in s:
        s = s.replace('01', '2302', 1)
        s = s.replace('02', '10', 1)
        s = s.replace('03', '201', 1)
    return s


def count_digits(s):
    return s.count('1'), s.count('2'), s.count('3')


for x in range(1000):
    initial_string = '0' + '1' * x + '2' * 10 + '3' * 8
    final_string = transform(initial_string)
    ones, twos, threes = count_digits(final_string)

    if ones == 40 and twos == 10 and threes == 8:
        print(x)
        break
