f= lambda x,y: x+y
print(f(2,3))

def sum (x,y):  #primer funkcijeu mesto lambade
    return(x+y)

print(sum(2,3))#primer funkcijeu mesto lambade



def broj(x):
    return x+x
brojevi=[1,2,3,4,5,]

print(list(map(broj,brojevi)))            #1 opcija
print(list(map(lambda x: x+x,brojevi)))   #lambda opcija



 #uz funkciju (map)nad svakim elementom ove lista pozvace se funkcija sabiranja



ghost=lambda x: 'positive' if x>0 else'negative'
ghost(5)
print(ghost(-5))



def filter_func(x):
    if x % 2:
        return True
    else:
        return False
 
numbers= list(range(0,10))
print(list(filter(filter_func, numbers)))
print(list(filter(lambda x: x % 2, numbers)))

