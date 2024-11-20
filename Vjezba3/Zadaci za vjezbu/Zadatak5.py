"""Definirajte korutinu secure_data koja će simulirati enkripciju osjetljivih podataka. Kako se u
praksi enkripcija radi na poslužiteljskoj strani, korutina će simulirati enkripciju podataka u trajanju od 3
sekunde. Korutina prima kao argument rječnik osjetljivih podataka koji se sastoji od ključeva prezime,
broj_kartice i CVV. Definirajte listu s 3 rječnika osjetljivih podataka. Pohranite u listu zadaci kao u
prethodnom zadatku te pozovite zadatke koristeći asyncio.gather(). Korutina secure_data mora za
svaki rječnik vratiti novi rječnik u obliku: {'prezime':prezime , 'broj_kartice': 'enkriptirano',
'CVV': 'enkriptirano'}. Za fake enkripciju koristite funkciju hash(str) koja samo vraća hash
vrijednost ulaznog stringa."""

import asyncio

async def secure_data(podatak):
    print("Početak enkripcije!")
    print(podatak["prezime"])
    await asyncio.sleep(3)
    enkriptirano=[{'prezime':podatak["prezime"] , 'broj_kartice':hash(podatak["broj_kartice"]) ,'CVV': hash(podatak["CVV"])}]
    return enkriptirano

async def main():
    podaci=[{"prezime":"Anić", "broj_kartice":"1234123412341234", "CVV":"123"},
             {"prezime":"Perić", "broj_kartice":"5678567856785678", "CVV":"567"},
             {"prezime":"Berić", "broj_kartice":"9876987698769876", "CVV":"987"}]
    zadaci=[asyncio.create_task(secure_data(podatak)) for podatak in podaci]
    rez = await asyncio.gather(*zadaci)
    print(rez)

asyncio.run(main())