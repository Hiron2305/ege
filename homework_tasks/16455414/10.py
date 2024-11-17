letters = ["А", "К", "Р", "У"]

tar = 0

for x in letters:
    for y in letters:
        for k in letters:
            for h in letters:
                for o in letters:
                    if tar < 450:
                        tar += 1
                        print(x, y, k, h, o, tar)
