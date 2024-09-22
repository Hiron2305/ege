def max_length_without_adjacent_a_d(filename):
    with open(filename, 'r') as file:
        text = file.read().strip()

    max_length = 0
    current_length = 0

    for i in range(len(text)):
        if i > 0 and ((text[i] == 'a' and text[i - 1] == 'd') or (text[i] == 'd' and text[i - 1] == 'a')):
            max_length = max(max_length, current_length)
            current_length = 0
        else:
            current_length += 1

    max_length = max(max_length, current_length)

    return max_length


filename = '24.txt'
result = max_length_without_adjacent_a_d(filename)
print(result)
