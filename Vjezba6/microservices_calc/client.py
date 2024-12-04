import asyncio
import aiohttp

async def fetch_1(brojevi):
    async with aiohttp.ClientSession() as session:
        res1= await session.post("http://localhost:8081/brojevi", json=brojevi)
        return await res1.text()

async def fetch_2(brojevi, zbroj):
    async with aiohttp.ClientSession() as session:
        podatak_koji_saljemo={"brojevi":brojevi, "zbroj":zbroj}
        res2= await session.post("http://localhost:8082/ratio", json=podatak_koji_saljemo)
        return await res2.text()


async def main():
        
    brojevi=[x for x in range(1,11)]
    zbroj=await fetch_1({"brojevi":brojevi})

    ratio = await fetch_2(brojevi, zbroj["zbroj"])

    print(zbroj,ratio )
asyncio.run(main())