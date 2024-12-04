import asyncio, aiohttp
from aiohttp import web

app=web.Application()

async def kolicnik_handler(request):
    data =await request.json()
    zbroj=data["zbroj"]
    umnozak=data["umnozak"]
    if(zbroj==0):
        return web.json_response(status=400, data={"error":"Zbroj je 0 - nemoguće djeljenje"})
    return web.json_response({"kolicnik":umnozak/zbroj})
    
app.router.add_post("/kolicnik", kolicnik_handler)


if __name__=="__main__":
    web.run_app(app, port=8085)