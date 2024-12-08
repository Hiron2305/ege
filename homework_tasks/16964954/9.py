from itertools import *

counter = 0
for i in product('012345678', repeat=5):
    s = ''.join(i)
    if s[0] != '0' and s.count('3') == 2:
        for j in s:
            if j in '1357': s = s.replace(j, '*')
        if '2*' not in s and '*2' not in s:
            counter += 1

print(counter)