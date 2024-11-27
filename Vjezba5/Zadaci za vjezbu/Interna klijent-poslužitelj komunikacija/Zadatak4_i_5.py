from aiohttp import web
from aiohttp.web import AppRunner
import asyncio, aiohttp

proizvodi = [
{"id": 1, "naziv": "Laptop", "cijena": 5000},
{"id": 2, "naziv": "Miš", "cijena": 100},
{"id": 3, "naziv": "Tipkovnica", "cijena": 200},
{"id": 4, "naziv": "Monitor", "cijena": 1000},
{"id": 5, "naziv": "Slušalice", "cijena": 50}]

narudzbe=[{"proizvod_id": 1,"kolicina": 2},{"proizvod_id": 2,"kolicina": 1},{"proizvod_id": 3,"kolicina": 5}]

async def get_proizvodi(req):
    proizvod_id = req.match_info.get("id")
    pronadeno=False
    if(proizvod_id):
        for proizvod in proizvodi:
            if(str(proizvod["id"]) == proizvod_id):
                trazeni_proizvod=proizvod
                pronadeno=True
        if(pronadeno):
            return web.json_response(trazeni_proizvod, status=200)
        else:
            return web.json_response({'error': 'Proizvod s traženim ID-em ne postoji'}, status=404)
            
    else:
        return web.json_response(proizvodi, status=200)
        
async def post_narudzba(req):
    data= await req.json()
    proizvod_id=data.get("proizvod_id")
    pronadeno=False
    if(proizvod_id):
        for proizvod in proizvodi:
            if(proizvod["id"] == proizvod_id):
                pronadeno=True
        if(pronadeno):
            narudzbe.append(data)
            return web.json_response(narudzbe, status=201)
        else:
            return web.json_response({'error': 'Proizvod s traženim ID-em ne postoji'}, status=404)
            

app = web.Application()

app.router.add_routes([web.get("/proizvodi", get_proizvodi),
                       web.get("/proizvodi/{id}", get_proizvodi),
                       web.post("/narudzbe", post_narudzba)])

async def start_server():
    runner = AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, 'localhost', 8081)
    await site.start()
    print("Poslužitelj radi!")

async def main():
    await start_server() 
    async with aiohttp.ClientSession() as session: 
        rezultat = await session.get('http://localhost:8081/proizvodi')
        rezultat_id = await session.get('http://localhost:8081/proizvodi/1')
        print("Get bez parametra: ", await rezultat.text())
        print("Get sa parametrom: ", await rezultat_id.text())

        nova_narudzba={"proizvod_id": 4,"kolicina": 1}

        nova_narudzba_rezultat=await session.post("http://localhost:8081/narudzbe",json=nova_narudzba)
        print("Post nova narudzba: ", await nova_narudzba_rezultat.text())
asyncio.run(main()) 