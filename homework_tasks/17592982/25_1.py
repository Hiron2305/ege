import fnmatch

for i in range(0, 100000000, 2622):
    if fnmatch.fnmatch(str(i), '1?4*6?8'):
        print(i, i/2622) 
