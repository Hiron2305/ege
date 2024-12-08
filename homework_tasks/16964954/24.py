def count_programs(start, target, checkpoint):
    from collections import defaultdict

    dp = defaultdict(int)
    dp[(0, start)] = 1

    reachable = set()
    reachable.add(start)

    for step in range(1, 100):
        for current in list(reachable):
            if dp[(step - 1, current)] > 0:
                next_num1 = current - 1
                if next_num1 >= 0:
                    dp[(step, next_num1)] += dp[(step - 1, current)]
                    reachable.add(next_num1)

                next_num2 = current // 3
                dp[(step, next_num2)] += dp[(step - 1, current)]
                reachable.add(next_num2)

    count = 0
    for step in range(1, 100):
        count += dp[(step, target)]

    if checkpoint in reachable:
        return count
    else:
        return 0

start_number = 67
target_number = 5
checkpoint_number = 33

result = count_programs(start_number, target_number, checkpoint_number)
print(result)
