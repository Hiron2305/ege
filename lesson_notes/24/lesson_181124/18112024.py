#72559
from itertools import *
t="12 14 19 21 27 34 35 36 41 43 46 49 53 58 63 64 67 68 72 76 78 85 86 87 91 94"
g="АБ БА АД ДА АГ ГА БВ ВБ БД ДБ ВЕ ЕВ ГЖ ЖГ ДЖ ЖД ДИ ИД ЕИ ИЕ ЕК КЕ ЖИ ИЖ КИ ИК"

s=set(g.replace(' ',''))
for p in permutations(s):
    nt=t
    for i,v in enumerate(p):
        nt=nt.replace(str(i+1),v)
    if set(g.split())==set(nt.split()):
        print (p)