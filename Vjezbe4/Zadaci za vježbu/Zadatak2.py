import time
import aiohttp
import asyncio

async def getCatFact(session):
    response=await session.get("https://catfact.ninja/fact")
    response_json=await response.json()
    return response_json["fact"]
         
async def filterCatFact(facts):
    filteredFacts=[fact for fact in facts if "cat" or "Cat" in fact]
    return filteredFacts
         

async def main():
    async with aiohttp.ClientSession() as session:

        tasks=[asyncio.create_task(getCatFact(session)) for _ in range(20)]
        rezultat = await asyncio.gather(*tasks)
        filteredResult=await asyncio.create_task(filterCatFact(rezultat))
        
        print ("Filtrirane činjenice o mačkama:")
        for fact in filteredResult:
            print("- ", fact)

asyncio.run(main())