letters = {0: "А", 1: "В", 2: "Л", 3: "О", 4: "Р"}
index = 0
for first in range(len(letters)):
    for second in range(len(letters)):
        for third in range(len(letters)):
            for fourth in range(len(letters)):
                index += 1
                if letters[first] == "Л":
                    print(index)
                    break
