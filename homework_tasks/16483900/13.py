def replace_in_string(s, v, w):
    return s.replace(v, w, 1)


def editor_program(s):
    while "00" not in s:
        s = replace_in_string(s, "01", "220")
        s = replace_in_string(s, "02", "1013")
        s = replace_in_string(s, "03", "120")
    return s


def find_max_length():
    for length in range(2, 1000):
        a = "0" + "1" * (length - 2) + "0"

        b = editor_program(a)

        ones = b.count("1")
        twos = b.count("2")

        if ones == 13 and twos == 18:
            return length

    return None


max_length = find_max_length()
print(max_length)
