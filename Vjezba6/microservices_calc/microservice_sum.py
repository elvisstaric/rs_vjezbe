import asyncio, aiohttp
from aiohttp import web

app=web.Application()

async def sum_handler(request):
    data =await request.json()
    brojevi=data["brojevi"]
    zbroj=sum(brojevi)
    return web.json_response({"zbroj":zbroj})

app.router.add_post("/brojevi", sum_handler)


if __name__=="__main__":
    web.run_app(app, port=8081)