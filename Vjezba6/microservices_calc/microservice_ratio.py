import asyncio, aiohttp
from aiohttp import web

app=web.Application()

async def ratio_handler(request):
    data =await request.json()
    brojevi=data["brojevi"]
    zbroj=data["zbroj"]
    ratio_list=[round(broj/zbroj, 2)for broj in brojevi]
    return web.json_response({"ratio":ratio_list})

app.router.add_post("/ratio", ratio_handler)


if __name__=="__main__":
    web.run_app(app, port=8082)