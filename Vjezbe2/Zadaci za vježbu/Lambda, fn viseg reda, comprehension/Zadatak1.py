#1.
kvadriraj= lambda x : x**2
print(kvadriraj(2))

#2.
zbroj_pa_kvadriranje = lambda a,b : (a+b)**2
print(zbroj_pa_kvadriranje(2,3))

#3.
niz=[1,2,3]
kvadriraj_duljinu_niza = lambda niz : len(niz)**2
print(kvadriraj_duljinu_niza(niz))

#4.
pomnozi_i_potenciraj = lambda x,y : (y*5)**x
print(pomnozi_i_potenciraj(2,2))

#5.
paran_broj = lambda x : True if(not x%2) else None
print(paran_broj(4))