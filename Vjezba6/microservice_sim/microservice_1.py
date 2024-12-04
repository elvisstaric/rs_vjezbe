import asyncio, aiohttp
from aiohttp import web

app=web.Application()

async def handler_service1(request):
    return web.json_response({"message":"Hello from microservice 1"})

app.router.add_get("/", handler_service1)


if __name__=="__main__":
    web.run_app(app, port=8081)