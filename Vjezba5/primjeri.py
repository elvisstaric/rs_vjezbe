import aiohttp
import asyncio
from aiohttp import web

#Servis
app=web.Application()

def handler_function(req):
    data={"ime":"Ivo"}
    return web.json_response(data, status=200)

async def handler_function_post(req):
    data = await req.json()
    print(data)
    return web.json_response(data, status=201)

app.router.add_get("/", handler_function)
app.router.add_post("/", handler_function_post)

"""
app.router.add_routes([web.get("/", handler)], [web.post("/", handler)])
"""

web.run_app(app, host="localhost", port= 3000) # app.listen() u JS

#Klijent

async def main():
    async with aiohttp.ClientSession() as session:
        print("Simulacija klijenta: ")
        res=session.get("http://localhost:3000/")
        print(res.json())

asyncio.run(main())