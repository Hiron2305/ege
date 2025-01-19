res = 0
with open("10_1.txt", encoding="utf-8") as file:
    a = file.read()
    res += a.count(" Он ") + a.count(" он ") + a.count(",он ") + a.count(" он,") + a.count(" он?") + a.count(" он.") + a.count(",Он ") + a.count(" Он,") + a.count(" Он?") + a.count(" Он.")

with open("10_2.txt", encoding="utf-8") as file:
    a = file.read()
    res += a.count(" Он ") + a.count(" он ") + a.count(",он ") + a.count(" он,") + a.count(" он?") + a.count(" он.") + a.count(",Он ") + a.count(" Он,") + a.count(" Он?") + a.count(" Он.")

print(res)