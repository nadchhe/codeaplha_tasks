def generatorFib():
    n2=1
    n3=1
    while True:
        n1=n2
        n2=n3
        n3=n1+n2
        yield n1
a =generatorFib()

for i in range(20):
    print (next(a), end=' ')