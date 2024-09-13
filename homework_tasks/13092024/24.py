def longest_valid_substring(s):
    valid_chars = set("0123456789ABCDEFGHIJKLMNOPQRSTUVWX")
    max_length = 0
    start = 0
    n = len(s)

    while start < n:
        end = start
        while end < n and s[end] in valid_chars:
            end += 1
        if start < end and (s[start] != '0' or start == end - 1):
            max_length = max(max_length, end - start)
        start = end + 1

    return max_length



s = open("24_59848.txt")
s = s.read()
print(longest_valid_substring(s))
