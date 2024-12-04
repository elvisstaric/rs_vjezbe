import asyncio
import aiohttp

async def fetch_1():
    async with aiohttp.ClientSession() as session:
        res1= await session.get("http://localhost:8081/pozdrav")
        return await res1.text()

async def fetch_2():
    async with aiohttp.ClientSession() as session:
        res2= await session.get("http://localhost:8082/pozdrav")
        return await res2.text()


async def main():
    
    pozdrav1=await fetch_1()
    pozdrav2 = await fetch_2()
    print("Sekvencijalno:", pozdrav1, pozdrav2)

    rez_con=await asyncio.gather(fetch_1(), fetch_2())
    print("Konkurentno:", rez_con)
asyncio.run(main())