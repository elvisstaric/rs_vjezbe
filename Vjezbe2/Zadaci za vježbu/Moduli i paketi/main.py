from shop import proizvodi as pr
from shop import narudzbe as nr

proizvodi = [
{"naziv": "Laptop", "cijena": 5000, "kolicina": 10},
{"naziv": "Monitor", "cijena": 1000, "kolicina": 20},
{"naziv": "Tipkovnica", "cijena": 200, "kolicina": 50},
{"naziv": "Miš", "cijena": 100, "kolicina": 100}
]

for proizvod in proizvodi:
    pr.dodaj_proizvod(proizvod["naziv"], proizvod["cijena"], proizvod["kolicina"])

for proizvod in pr.proizvodi:
    proizvod.ispis()

nr.napravi_narudzbu([{"naziv": "Laptop", "cijena": 5000, "kolicina": 1},{"naziv": "Miš", "cijena": 100, "kolicina": 2}])

for narudzba in nr.narudzbe:
    narudzba.ispis_narudzbe()
