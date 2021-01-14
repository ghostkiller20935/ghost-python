def parni_brojevi(a):
    for x in range(a):
        if x%2==0:
            yield x
for e in parni_brojevi(10):
     print(e)