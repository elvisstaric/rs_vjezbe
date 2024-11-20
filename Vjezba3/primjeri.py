import asyncio

#sleep, gather
async def fetch_api1():
    print("Dohvacam podatke s API-ja 1")
    await asyncio.sleep(2)
    print("Podatci s API1 uspješno odhvaćeni")
    return {"api1":"uspješno"}

async def fetch_api2():
    print("Dohvacam podatke s API-ja 2")
    await asyncio.sleep(3)
    print("Podatci s API1 uspješno odhvaćeni")
    return {"api2":"uspješno"}

async def timer(name, delay):
    print(f"pocinje timer {name}...")
    for i in range(delay, 0, -1):
        await asyncio.sleep(1)
    print(f"timer {name} gotov")


async def korutina(n):
    await asyncio.sleep(1)
    return f"Korutina {n} je završila"


async def main():

    #rez_sve = await asyncio.gather(fetch_api1(), fetch_api2())
    #print(rez_sve)
    #tim= await asyncio.gather(timer("1",5), timer("2", 2))
    #task1=asyncio.create_task(fetch_api1())
    #task2=asyncio.create_task(fetch_api2())

    #podatci_1=await task1
    #podatci_2=await task2
    #-nije potrebnoi stavljati u gather kada su taskovi - izvode se konkurentno

    comp_lista=[asyncio.create_task(korutina(i)) for i in range (1,6)]
    res=await asyncio.gather(*comp_lista)
    print(res)
asyncio.run(main())