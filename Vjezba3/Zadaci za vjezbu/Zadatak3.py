"""Definirajte korutinu autentifikacija() koja će simulirati autentifikaciju korisnika na
poslužiteljskoj strani. Korutina kao ulazni parametar prima rječnik koji opisuje korisnika, a sastoji se
od ključeva korisnicko_ime , email i lozinka . Unutar korutine simulirajte provjeru korisničkog
imena na način da ćete provjeriti nalaze li se par korisnicko_ime i email u bazi korisnika. Ova
provjera traje 3 sekunde."""

import asyncio

baza_korisnika = [
{'korisnicko_ime': 'mirko123', 'email': 'mirko123@gmail.com'},
{'korisnicko_ime': 'ana_anic', 'email': 'aanic@gmail.com'},
{'korisnicko_ime': 'maja_0x', 'email': 'majaaaaa@gmail.com'},
{'korisnicko_ime': 'zdeslav032', 'email': 'deso032@gmail.com'}
]

baza_lozinka = [
{'korisnicko_ime': 'mirko123', 'lozinka': 'lozinka123'},
{'korisnicko_ime': 'ana_anic', 'lozinka': 'super_teska_lozinka'},
{'korisnicko_ime': 'maja_0x', 'lozinka': 's324SDFfdsj234'},
{'korisnicko_ime': 'zdeslav032', 'lozinka': 'deso123'}
]

async def auentifikacija(kor):
    print("Pocetak provjere")
    await asyncio.sleep(3)
    for korisnik in baza_korisnika:
        if korisnik["korisnicko_ime"]==kor["korisnicko_ime"] and korisnik["email"]==kor["email"]:
            postoji=await autorizacija(kor, baza_lozinka)

        else:
            postoji=f"Korinik {kor['korisnicko_ime']} ne postoji!"
    print("Provjera zavrsena!")
    return postoji

async def autorizacija(korisnik, baza_loz):
    print("Pocetak provjere lozinke")
    await asyncio.sleep(2)
    for korisnik_loz in baza_loz:
        if korisnik_loz["lozinka"] == korisnik["lozinka"]:
            postoji=f"Korisnik {korisnik["korisnicko_ime"]}: Autorizacija uspješna."
        else:
            postoji= f"Korisnik {korisnik["korisnicko_ime"]}: Autorizacija neuspješna."
    print("provjera lozinke gotova!")
    return postoji
        


async def main():
    rez=await auentifikacija(
{'korisnicko_ime': 'zdeslav032', 'email': 'deso032@gmail.com', "lozinka":"deso1234"})
    print(rez)
asyncio.run(main())