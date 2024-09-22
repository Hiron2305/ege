def F(n):
    if n < 11:
        return n
    else:
        result = 0
        for i in range(11, n + 1):
            result += i
        return result + 10

result = F(2024) - F(2021)
print(result)
