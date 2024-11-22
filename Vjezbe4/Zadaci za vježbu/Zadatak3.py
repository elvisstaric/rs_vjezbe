import time
import aiohttp
import asyncio

async def getDogFact(session):
    response=await session.get("https://dogapi.dog/api/v2/facts")
    response_json=await response.json()
    return response_json["data"][0]["attributes"]["body"]

async def getCatFact(session):
    response=await session.get("https://catfact.ninja/fact")
    response_json=await response.json()
    return response_json["fact"]

async def mixed_facts(dog_facts, cat_facts):
    mixed_facts=[]
    for i in range(5):
        if len(dog_facts[i])>len(cat_facts[i]):
            mixed_facts.append(dog_facts[i])
        else:
            mixed_facts.append(cat_facts[i])
    return mixed_facts
         

         

async def main():
    async with aiohttp.ClientSession() as session:

        dog_fact_taks=[asyncio.create_task(getDogFact(session)) for _ in range(5)]
        cat_fact_task=[asyncio.create_task(getCatFact(session)) for _ in range(5)]

        rezultat=await asyncio.gather(*dog_fact_taks, *cat_fact_task)
       
        dog_facts=rezultat[0:5]
        cat_facts=rezultat[5:10]
        mixed_rezultat=  await asyncio.create_task(mixed_facts(dog_facts,cat_facts))

        print("Mixane činjenice o psima i mačkama:",)
        for mixed_fact in mixed_rezultat:
            print("- ", mixed_fact)
       

asyncio.run(main())