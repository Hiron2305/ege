string = "02122333210"

while "00" not in string:
    string = string.replace("01", "220")
    print(string)
    string = string.replace("02", "1013")
    print(string)
    string = string.replace("03", "120")
    print(string)
