def longest_valid_substring(s):
    valid_chars = set("09-")
    max_length = 0
    start = 0
    n = len(s)

    while start < n:
        end = start
        while end < n and s[end] in valid_chars:
            end += 1
        if max_length < end - start:
            max_str = s[start:end]
        max_length = max(max_length, end - start)
        start = end + 1

    return (max_length, max_str)



s = open("24_3.txt")
s = s.read()
s = s.replace('*', '-').replace('--', '- -')
s = s.replace('6', '9').replace('7', '9').replace('8', '9')
s = s.replace('-09', '-0 9')
s = s.replace(' -9', ' - 9').replace('9- ', '9 - ').replace('0- ', '0 - ')
print(longest_valid_substring(s))
