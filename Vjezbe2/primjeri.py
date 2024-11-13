#MAP
#map(function, iterables) - primjeni fn na svaki el
lista=[1,2,3]

lista_kvad=list(map(lambda x: x*x, lista))
print(lista_kvad)


studenti=[{"ime":"a", "prez":"b", "jmbag":5621616, "gr":1998}, {"ime":"aa", "prez":"bb", "jmbag":5621616, "gr":2003}]

lista_jmbagova=list(map(lambda st:st["jmbag"], studenti))

print(lista_jmbagova)

#FILTER
#filter(function, iterables) - vraca manju listu ovisno o uvjetu- list ase mora sastojati od bool

list_nr=[1,2,3,4,5,6,7,8,9,10]

rez=(list(filter(lambda x: not x%2, list_nr)))
print(rez)

rezst=(list(filter(lambda st: st["gr"]<2000, studenti)))
print(rezst)


#any/all-True/False ako je jedan/svi elemnti liste istiniti
sviparni=all( list(map(lambda x:not x%2, list_nr)))
print(sviparni)

#list comp
list_kvadrata=[x**2 for x in list_nr]
print(list_kvadrata)
nizovi=["jabuka", "kruškaa"]

list_diljina=[len(x) for x in nizovi]
print(list_diljina)

brojevi=[32, 45, 675, 55, 1, 22]

list_parni=[x for x in brojevi if not x%2]
print(list_parni)

paran_neparan=[x**2 if not x%2 else x**3 for x in brojevi]
print(paran_neparan)

imena_st_prije_99=[st["ime"] for st in studenti if st["gr"]<1999]
print(imena_st_prije_99)


#dict compr
#{key_expression:val for item in iterable if con}

dict_comp={voce:len(voce) for voce in nizovi}
print(dict_comp)