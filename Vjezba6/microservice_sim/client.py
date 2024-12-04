import asyncio
import aiohttp

async def main():
    async with aiohttp.ClientSession() as session:
        res1= await session.get("http://localhost:8081/")
        res2= await session.get("http://localhost:8003/")
        
        
        res1_json = await res1.text()
        res2_json = await res2.text()

    print(res1_json, res2_json)
asyncio.run(main())