pomnozi_i_potenciraj= lambda x,y: (y * 5) ** x

print(pomnozi_i_potenciraj(2,3))

#Koristeći funkcije all i map, provjerite jesu li svi studenti punoljetni:

studenti = [
    {"ime": "Ivan", "prezime": "Ivić", "godine": 19},
    {"ime": "Marko", "prezime": "Marković", "godine": 22},
    {"ime": "Ana", "prezime": "Anić", "godine": 21},
    {"ime": "Petra", "prezime": "Petrić", "godine": 13},
    {"ime": "Iva", "prezime": "Ivić", "godine": 17},
    {"ime": "Mate", "prezime": "Matić", "godine": 18}
]

svi_punoljetni=all(list(map(lambda st:st["godine"]>18,studenti)))
print(svi_punoljetni)

kubovi_bez_uvjeta={broj:broj**3 for broj in range(1,11)}
print(kubovi_bez_uvjeta)

kubovi_sa_uvjetom= {broj:(broj**3 if broj%2!=0 else broj) for broj in range(1,11) }
print(kubovi_sa_uvjetom)