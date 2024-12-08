from itertools import *
from time import *

def fu1():
    s="ABCD"
    for x in permutations(s,4):
        s="".join(x)
        print(*x,x,s)



def k(x,y,z,w):
    print (x,y,z,w)

def fu2():
    s="1010"
    k=('x','y','z','w')
    # for x in permutations(s,4):
    #     # s="".join(x)
    #     # print(*x,x,s)
    m=dict(zip(k,s))
    print(m)
    # k(**m)

    # for x in **m:
    #     print x
    # print(m)


def fu3():

    def f(x, y, z, w):
        return ((x and (not y)) == (z or (not w))) <= (x and z)

    for a1, a2, a3, a4, a5, a6 in product([0, 1], repeat=6):
        tab = [(1, a1, 1, 1), (1, a2, 1, a3), (a4, a5, 1, a6)]
        print(tab, len(tab), len(set(tab)))
        if len(tab) == len(set(tab)):
            for p in permutations('xyzw'):
                if [f(**dict(zip(p, r))) for r in tab] == [0, 0, 0]:
                    print(p)


def my_function(school, standard, city, name):
    print (school,standard,city,name)


a=('school','standard','name','city')
b=('DAV','7','abc','delhi')
m=dict(zip(a,b))
my_function(**m)

# data = {'school':'DAV', 'standard': '7', 'name': 'abc', 'city': 'delhi'}
# my_function(**data)

# fu4(**a)
# ts=time()
# fu2()
# print(time()-ts)

a=[[1,2],[3,4],[5,6]]
print (*a)
# b=list(zip(*a))
# print (b)