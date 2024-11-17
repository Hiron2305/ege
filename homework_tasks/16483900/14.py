alph = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alph[:9]:
    for y in alph[:9]:
        A = int(f'{x}341{y}', 11)
        B = int(f'56{x}1{y}', 19)
        print((A+B) / 305)