import asyncio, aiohttp
from aiohttp import web

app=web.Application()

async def handler_service1(request):
    await asyncio.sleep(3)
    return web.json_response({"message":"Pozdrav nakon 3 sekunde"})

app.router.add_get("/pozdrav", handler_service1)


if __name__=="__main__":
    web.run_app(app, port=8081)