import requests as req
import time
import aiohttp
import asyncio


"""def sedn_req():
    print("Šalje se zahtjev")
    res=req.get("https://catfact.ninja/fact")
    odg=res.text
    print(odg)
    return odg"""

"""start_time=time.time()
for  i in range(5):
    sedn_req()

end_time=time.time()
print(f"Vrijeme izvodenja {end_time-start_time}")"""

#Asinkrono

async def getCatFact(session):
    response=await session.get("https://catfact.ninja/fact")
    response_json=await response.json()
    print(response_json)
    return response_json
         

async def main():
    async with aiohttp.ClientSession() as session:

        lista_korutina=[getCatFact(session) for i in range(5)]
        rezultat = await asyncio.gather(*lista_korutina)

        print(rezultat)

asyncio.run(main())
