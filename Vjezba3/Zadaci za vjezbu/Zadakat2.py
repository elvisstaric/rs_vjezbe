"""Definirajte dvije korutine koje će simulirati dohvaćanje podataka s weba. Prva korutina neka vrati
listu proizvoljnih rječnika (npr. koji reprezentiraju podatke o korisnicima) nakon 3 sekunde, a druga
korutina neka vrati listu proizvoljnih rječnika (npr. koji reprezentiraju podatke o proizvodima) nakon 5
sekundi. Korutine pozovite konkurentno korištenjem asyncio.gather() i ispišite rezultate. Program
se mora izvršavati ~5 sekundi."""

import asyncio



async def lista_korisnika():
    baza_korisnika = [
{'korisnicko_ime': 'mirko123', 'email': 'mirko123@gmail.com'},
{'korisnicko_ime': 'ana_anic', 'email': 'aanic@gmail.com'},
{'korisnicko_ime': 'maja_0x', 'email': 'majaaaaa@gmail.com'},
{'korisnicko_ime': 'zdeslav032', 'email': 'deso032@gmail.com'}]
    print("Dohvacam podatke s API-ja - korisnici")
    await asyncio.sleep(3)
    print("Podatci o korisnicima dohvaćeni")
    print (baza_korisnika)
    return baza_korisnika

async def lista_proizvoda():
    baza_proizvoda = [
    {"proizvod":"proizvod1", "zaliha":1},
    {"proizvod":"proizvod2", "zaliha":2},
    {"proizvod":"proizvod3", "zaliha":3},
    ]
    print("Dohvacam podatke s API-ja - korisnici")
    await asyncio.sleep(5)
    print("Podatci o korisnicima dohvaćeni")
    return baza_proizvoda

async def main():

    res=await asyncio.gather(lista_korisnika(), lista_proizvoda())
    print(res)
asyncio.run(main())