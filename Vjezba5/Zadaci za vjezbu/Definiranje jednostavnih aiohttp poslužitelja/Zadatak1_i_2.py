import aiohttp
import asyncio
from aiohttp import web


app=web.Application()

def get_proizvodi(req):
    data=[{"naziv":"P1", "cijena":10, "kolicina":10},
          {"naziv":"P2", "cijena":20, "kolicina":10},
          {"naziv":"P3", "cijena":30, "kolicina":10},
          {"naziv":"P4", "cijena":40, "kolicina":10}]
    return web.json_response(data, status=200)

async def post_proizvodi(req):
    data=await req.json()
    return web.json_response(data, status=201)


app.router.add_routes([web.get("/proizvodi", get_proizvodi),web.post("/proizvodi", post_proizvodi)])


web.run_app(app, host="localhost", port= 8081)