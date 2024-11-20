"""Definirajte korutinu provjeri_parnost koja će simulirati "super zahtjevnu operaciju" provjere
parnosti broja putem vanjskog API-ja. Korutina prima kao argument broj za koji treba provjeriti
parnost, a vraća poruku "Broj {broj} je paran." ili "Broj {broj} je neparan." nakon 2 sekunde.
Unutar main funkcije definirajte listu 10 nasumičnih brojeva u rasponu od 1 do 100 (koristite random
modul). Listu brojeva izgradite kroz list comprehension sintaksu. Nakon toga, pohranite u listu zadaci
10 Task objekata koji će izvršavati korutinu provjeri_parnost za svaki broj iz liste (također kroz list
comprehension). Na kraju, koristeći asyncio.gather() , pokrenite sve korutine konkurentno i ispišite
rezultate."""

import asyncio
import random

async def provjeri_parnost(broj):
    print("Pocetak provjere parnosti!")
    await asyncio.sleep(2) 
    if (not broj%2): 
        paran=f"Broj {broj} je paran"
    else:
        paran=f"Broj {broj} je neparan"
    print("Provjera parnosti gotova")
    return paran

async def main():
    lista_brojeva=[random.randint(1,100) for _ in range(1,11)]
    print("Lista brojeva: ", lista_brojeva)
    zadatci = [asyncio.create_task(provjeri_parnost(i)) for i in lista_brojeva]
    rez = await asyncio.gather(*zadatci)
    print("Rezultat: ", rez)

asyncio.run(main())