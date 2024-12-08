from fnmatch import fnmatch

upper_limit = 10 ** 9
step = 2031

for number in range(0, upper_limit + 1, step):
    if fnmatch(str(number), '*31*65?') and number % 31 == 0:
        divisors = []

        for potential_divisor in range(1, int(number ** 0.5) + 1):
            if number % potential_divisor == 0:
                divisors.append(potential_divisor)
                if potential_divisor != (number // potential_divisor):
                    divisors.append(number // potential_divisor)

        for power in range(100):
            if len(divisors) == 2 ** power:
                print(number, number // step)
                break
