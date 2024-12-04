import asyncio
import aiohttp

brojevi={"brojevi":[x for x in range(1,5)]}

async def fetch_sum():
    async with aiohttp.ClientSession() as session:
        res_sum= await session.post("http://localhost:8083/zbroj", json=brojevi)
        return (res_sum.status, await res_sum.json())

async def fetch_umnozak():
    async with aiohttp.ClientSession() as session:
        res_umnozak= await session.post("http://localhost:8084/umnozak", json=brojevi)
        return (res_umnozak.status, await res_umnozak.json())

async def fetch_kolicnik(umnozak, zbroj):
    async with aiohttp.ClientSession() as session:
        zbroj_umnozak={"zbroj":zbroj, "umnozak":umnozak}
        res_kolicnik= await session.post("http://localhost:8085/kolicnik", json=zbroj_umnozak)
        return (res_kolicnik.status, await res_kolicnik.json())

async def main():
    
    res_sum_umnozak=await asyncio.gather(fetch_sum(), fetch_umnozak())
    print("Zbroj i umnozak: ", res_sum_umnozak)

    res_kolicnik=await fetch_kolicnik(res_sum_umnozak[1][1]["umnozak"], res_sum_umnozak[0][1]["zbroj"])
    print("Kolicnik: ", res_kolicnik)
asyncio.run(main())