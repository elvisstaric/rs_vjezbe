class Proizvod:
    def __init__(self, naziv, cijena, kolicina):
        self.naziv=naziv
        self.cijena=cijena
        self.kolicina=kolicina
    def ispis(self):
        print(f"Proizvod: {self.naziv}, cijena: {self.cijena}, kolicina: {self.kolicina}")

proizvodi=[Proizvod("proizvod1", 100, 200), Proizvod("proizvod2", 500, 50)]

def dodaj_proizvod(naziv, cijena, kolicina):
    proizvodi.append(Proizvod(naziv, cijena, kolicina))
