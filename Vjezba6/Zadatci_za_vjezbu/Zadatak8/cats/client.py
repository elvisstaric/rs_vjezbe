import asyncio
import aiohttp

brojevi={"brojevi":[x for x in range(1,5)]}

async def fetch_cat_facts():
    async with aiohttp.ClientSession() as session:
        res_cats= await session.get("http://localhost:8086/cats/10")
        return await res_cats.json()

async def filter_cat_facts(data):
    async with aiohttp.ClientSession() as session:
        res_cat_filtered= await session.post("http://localhost:8087/facts", json=data)
        return await res_cat_filtered.json()


async def main():
    
    res_cat_facts=await fetch_cat_facts()
    print("Cat facts: ", res_cat_facts)

    res_filtered_facts=await filter_cat_facts(res_cat_facts)
    print("Filtered cat facts: ", res_filtered_facts)


asyncio.run(main())