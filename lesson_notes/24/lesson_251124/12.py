def found(string, v):
    return str(v) in string


def change(v, w, string):
    if str(v) in string:
        string = string.replace(str(v), str(w), 1)
    return string

def check(string, i):
    counter = 0
    while found(string, 111):
        #print("repeated:", counter)
        string = change(111,2, string)
        string = change(222,11,string)
        string = change(1,2,string)
        #counter += 1
    if string.find("1") == 0 and len(string) > 0:
        print(string, i)

        for index in range():
            pass

for i in range(100, 200):
    check(str("1" * i), i)

