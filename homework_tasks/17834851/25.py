import fnmatch

for i in range(0, 10000000000, 3147):
    if fnmatch.fnmatch(str(i), '1*4239?7'):
        print(i, i/3147)
