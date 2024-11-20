import asyncio
"""Definirajte korutinu koja će simulirati dohvaćanje podataka s weba. Podaci neka budu lista
brojeva od 1 do 10 koju ćete vratiti nakon 3 sekunde. Listu brojeva definirajte comprehensionom.
Nakon isteka vremena, u korutinu ispišite poruku "Podaci dohvaćeni." i vratite podatke. Riješite bez
korištenja asyncio.gather() i asyncio.create_task() funkcija."""


async def list_fetch():
    data=[x for x in range (1,11)]
    print("Dohvacam podatke s API-ja")
    await asyncio.sleep(3)
    print("Podatci dohvaćeni")
    return data

async def main():
    rez=await list_fetch()
    print(rez)
asyncio.run(main())