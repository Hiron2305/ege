import re
import itertools


def generate_numbers(mask):
    fixed_part = re.sub(r'[?*]', '', mask)
    star_positions = [m.start() for m in re.finditer(r'\*', mask)]
    question_positions = [m.start() for m in re.finditer(r'\?', mask)]

    for star_replacements in itertools.product('0123456789', repeat=10):
        for question_replacements in itertools.product('0123456789', repeat=len(question_positions)):
            num_list = list(mask)
            for i, pos in enumerate(star_positions):
                num_list[pos] = star_replacements[i]
            for i, pos in enumerate(question_positions):
                num_list[pos] = question_replacements[i]
            generated_number = ''.join(num_list)
            if len(generated_number) > 10 or int(generated_number) > 10 ** 10:
                continue
            yield int(generated_number)


def find_valid_numbers(mask, divisor):
    valid_numbers = []
    for number in generate_numbers(mask):
        if number % divisor == 0:
            valid_numbers.append(number)
    return sorted(valid_numbers)


mask = '1*4022?9'
divisor = 1987

results = find_valid_numbers(mask, divisor)

for number in results:
    print(number)
