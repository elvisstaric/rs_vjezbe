import asyncio, aiohttp
from aiohttp import web

app=web.Application()

async def getCatFact(session):
    response=await session.get("https://catfact.ninja/fact")
    response_json=await response.json()
    return response_json["fact"]

async def get_cat_facts(request):
    nr_facts=int(request.match_info.get("amount"))
    async with aiohttp.ClientSession() as session:
        facts=[asyncio.create_task(getCatFact(session)) for _ in range(nr_facts)]
        rez_facts = await asyncio.gather(*facts)
    return web.json_response({"facts":rez_facts})
   
  

app.router.add_get("/cats/{amount}", get_cat_facts)


if __name__=="__main__":
    web.run_app(app, port=8086)