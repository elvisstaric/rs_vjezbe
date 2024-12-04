import asyncio, aiohttp
from aiohttp import web

app=web.Application()

async def umnozak_handler(request):
    try:
        data =await request.json()
        brojevi=data["brojevi"]
        umnozak=1
        for broj in brojevi:
            umnozak*=broj      
        return web.json_response({"umnozak":umnozak})
    except:
        return web.json_response(data={"error":"Lista brojeva nije poslana!"}, status=400)
  

app.router.add_post("/umnozak", umnozak_handler)


if __name__=="__main__":
    web.run_app(app, port=8084)