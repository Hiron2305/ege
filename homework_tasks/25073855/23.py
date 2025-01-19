def count_programs(current, has_19, has_29):
    if current == 6:
        return int(has_19 and has_29)
    if current < 6 or current in (24,):
        return 0

    ways = count_programs(current - 1, has_19 or current == 19, has_29 or current == 29)
    ways += count_programs(current - 6, has_19 or current == 19, has_29 or current == 29)
    ways += count_programs(current // 2, has_19 or current == 19, has_29 or current == 29)

    return ways

result = count_programs(34, False, False)
print(result)
