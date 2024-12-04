import asyncio, aiohttp
from aiohttp import web

app=web.Application()

async def handler_service2(request):
    await asyncio.sleep(4)
    return web.json_response({"message":"Pozdrav nakon 4 sekunde"})

app.router.add_get("/pozdrav", handler_service2)


if __name__=="__main__":
    web.run_app(app, port=8082)