import aiohttp
import asyncio
from aiohttp import web


app=web.Application()

korisnici = [
{'ime': 'Ivo', 'godine': 25},
{'ime': 'Ana', 'godine': 17},
{'ime': 'Marko', 'godine': 19},
{'ime': 'Maja', 'godine': 16},
{'ime': 'Iva', 'godine': 22}]

def get_punoljetni(req):
    punoljetni=list(filter(lambda korisnik : korisnik["godine"]>18 ,korisnici))
    return web.json_response(punoljetni, status=200)


app.router.add_get("/punoljetni", get_punoljetni)


web.run_app(app, host="localhost", port= 8082)