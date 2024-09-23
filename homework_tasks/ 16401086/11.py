def check_prime(num):
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    return True

for n in range(69, 100):
    result = n * 3 - 1
    if check_prime(result):
        print(n)
        break
