import math

#1.
parni_kvadrati = [x**2 for x in range(20,51) if (x**2) % 2 == 0]
print(parni_kvadrati)

#2.
rijeci = ["jabuka", "pas", "knjiga", "zvijezda", "prijatelj", "zvuk", "čokolada", "ples", "pjesma", "otorinolaringolog"]
duljine_sa_slovom_a =[len(rijec) for rijec in rijeci if "a" in rijec]
print(duljine_sa_slovom_a)

#3.
kubovi = [{broj:broj**3} if broj%2!=0 else {broj:broj} for broj in range(1,11)]
print(kubovi) 

#4.
korijeni = {broj:round(math.sqrt(broj),2) for broj in range(50,501,50)}
print(korijeni) # {50: 7.07, 100: 10.0, 150: 12.25, 200: 14.14, 250: 15.81, 300: 17.32,350: 18.71, 400: 20.0, 450: 21.21, 500: 22.36}

#5.
studenti = [
{"ime": "Ivan", "prezime": "Ivić", "bodovi": [12, 23, 53, 64]},
{"ime": "Marko", "prezime": "Marković", "bodovi": [33, 15, 34, 45]},
{"ime": "Ana", "prezime": "Anić", "bodovi": [8, 9, 4, 23, 11]},
{"ime": "Petra", "prezime": "Petrić", "bodovi": [87, 56, 77, 44, 98]},
{"ime": "Iva", "prezime": "Ivić", "bodovi": [23, 45, 67, 89, 12]},
{"ime": "Mate", "prezime": "Matić", "bodovi": [75, 34, 56, 78, 23]}]

zbrojeni_bodovi = [(student["prezime"], sum(student["bodovi"])) for student in studenti]
print(zbrojeni_bodovi)