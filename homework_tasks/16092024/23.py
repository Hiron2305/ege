def count_programs(start, target):
    dp = [0] * (target + 1)

    dp[start] = 1

    for i in range(start, target + 1):
        if i + 1 <= target:
            dp[i + 1] += dp[i]
        if i + 10 <= target:
            dp[i + 10] += dp[i]

    return dp[target]


start_number = 10
target_number = 32

result = count_programs(start_number, target_number)
print(result)
