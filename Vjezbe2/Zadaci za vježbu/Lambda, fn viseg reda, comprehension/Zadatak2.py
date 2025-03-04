#1.
nizovi = ["jabuka", "kruška", "banana", "naranča"]
kvadrirane_duljine = list(map(lambda el:len(el)**2, nizovi))
print(kvadrirane_duljine)

#2.
brojevi = [1, 21, 33, 45, 2, 2, 1,-32, 9, 10]
veci_od_5 = list(filter(lambda broj:broj>5, brojevi))
print(veci_od_5)

#3.
brojevi = [10, 5, 12, 15, 20]
transform = dict(map(lambda broj: (broj,broj**2), brojevi))
print(transform) 

#4.
studenti = [
{"ime": "Ivan", "prezime": "Ivić", "godine": 19},
{"ime": "Marko", "prezime": "Marković", "godine": 22},
{"ime": "Ana", "prezime": "Anić", "godine": 21},
{"ime": "Petra", "prezime": "Petrić", "godine": 13},
{"ime": "Iva", "prezime": "Ivić", "godine": 17},
{"ime": "Mate", "prezime": "Matić", "godine": 18}
]
svi_punoljetni = all(list(map(lambda student: student["godine"]>18, studenti)))
print(svi_punoljetni) 

#5.
rijeci = ["jabuka", "pas", "knjiga", "zvijezda", "prijatelj", "zvuk","čokolada", "ples","pjesma", "otorinolaringolog"]
min_duljina = int(input("Unesite minimalnu duljinu riječi: "))
duge_rijeci = list(filter(lambda rijec:len(rijec)>min_duljina , rijeci))
print(duge_rijeci) 
