from fastapi import FastAPI

from routers.filmovi import router as movies_router

app=FastAPI()
app.include_router(movies_router)
