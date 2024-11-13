from shop import proizvodi as pr

class Narudzba:
    def __init__(self, proizvodi, ukupna_cijena):
        self.proizvodi=proizvodi
        self.ukupna_cijena=ukupna_cijena
    def ispis_narudzbe(self):
        ispis=""
        for proizvod in self.proizvodi:
            ispis+=proizvod["naziv"] + " x " + str(proizvod["kolicina"])+", "
        print(f"Naruceni proizvodi: {ispis}. Ukupna cijena: {self.ukupna_cijena} eur")

narudzbe=[]

def napravi_narudzbu(lista_proizvoda):
    narudzba_proizvodi=[]
    ukupna_cijena=0
    if(type(lista_proizvoda==list)):
        if(lista_proizvoda):
                for proizvod in lista_proizvoda:
                    if(type(proizvod==dict)):
                        if("naziv" in proizvod and "cijena" in proizvod and "kolicina" in proizvod):
                            for proizvod_stanje in pr.proizvodi:
                                if(proizvod_stanje.naziv==proizvod["naziv"]):
                                    if(proizvod_stanje.kolicina<1):
                                        print(f"Proizvod {proizvod["naziv"]} nije dostupan")
                                        return
                                    else:
                                        narudzba_proizvodi.append({"naziv": proizvod["naziv"], "kolicina":proizvod["kolicina"]})
                                        ukupna_cijena+=(proizvod["kolicina"]*proizvod["cijena"])
                narudzbe.append(Narudzba(narudzba_proizvodi, ukupna_cijena))

