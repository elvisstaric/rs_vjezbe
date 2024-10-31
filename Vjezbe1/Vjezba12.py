rjecnik = {"ime": "Ivan", "prezime": "Ivić", "dob": 25}

def obrni_rijecnik(rjecnik):
    for kljuc in rjecnik:
         val = rjecnik[kljuc]
         rjecnik[val]=rjecnik.pop(kljuc)
         rjecnik[val]=kljuc
    return rjecnik
print(obrni_rijecnik(rjecnik))