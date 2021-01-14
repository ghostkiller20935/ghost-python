

def menjaj_nadrugufunkciju(funkcija):  
    return drugafunkcija



def prvafunkcija():
    print('prva funkcija')


def drugafunkcija():
    print('druga funkcija')

prvafunkcija = menjaj_nadrugufunkciju(prvafunkcija)
print(prvafunkcija())

