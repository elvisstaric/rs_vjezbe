lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def parniBr(list):
    lista2=[]
    for element in lista:
        if(element%2==0):
            lista2.append(element)
    return lista2

a=parniBr(lista)
print(a)