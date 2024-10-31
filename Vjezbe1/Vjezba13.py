#1
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

prvi_i_zadnji=lambda lista : (lista[0],lista[-1])

print(prvi_i_zadnji(lista))

#2 
lista = [5, 10, 20, 50, 100, 11, 250, 50, 80]

def maks_i_min(lista):
    max=None
    min=None
    for i in lista:
        if max is None:
            max=i
        elif i>max:
            max=i
        if min is None:
            min=i
        elif i<min:
            min=i
    return(max, min)

print(maks_i_min(lista))

#3
skup_1 = {1, 2, 3, 4, 5}
skup_2 = {4, 5, 6, 7, 8}

presjek = lambda s1, s2 : s1.intersection(s2)

print(presjek(skup_1,skup_2))
