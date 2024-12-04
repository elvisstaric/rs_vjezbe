import asyncio, aiohttp
from aiohttp import web

app=web.Application()

async def filter_cat_facts(request):
    data = await request.json()
    facts=data["facts"]
    filteredFacts=[fact for fact in facts if "cat" or "Cat" in fact]
    return web.json_response({"filtered_facts":filteredFacts})
   
  

app.router.add_post("/facts", filter_cat_facts)


if __name__=="__main__":
    web.run_app(app, port=8087)