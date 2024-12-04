import asyncio, aiohttp
from aiohttp import web

app=web.Application()

async def sum_handler(request):
    try:
        data =await request.json()
        brojevi=data["brojevi"]
        zbroj=0
        for broj in brojevi:
            zbroj+=broj      
        return web.json_response({"zbroj":zbroj})
    except:
        return web.json_response(data={"error":"Lista brojeva nije poslana!"}, status=400)
  

app.router.add_post("/zbroj", sum_handler)


if __name__=="__main__":
    web.run_app(app, port=8083)