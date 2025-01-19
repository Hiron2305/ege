alph = ["К", "Л", "Р", "Т"]

counter = 0

for i in alph:
     for j in alph:
         for k in alph:
             for o in alph:
                 word = i + j + k + o
                 counter += 1
                 if counter == 67:
                     print(word)