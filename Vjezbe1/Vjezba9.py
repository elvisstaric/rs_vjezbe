lista=[1,2,3,4,4]
def ukloniDuplikate(listaOr):
    set1=set(listaOr)
    return list(set1)

print(ukloniDuplikate(lista))