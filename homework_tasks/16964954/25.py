with open('1_24.txt', 'r') as file:
    content = file.read()

current_count = 1
maximum_count = 0

for index in range(1, len(content)):
    if (content[index - 1] not in 'QRW' or content[index] not in 'QRW') and (content[index - 1] not in '124' or content[index] not in '124'):
        current_count += 1
    else:
        maximum_count = max(maximum_count, current_count)
        current_count = 1

print(maximum_count)
