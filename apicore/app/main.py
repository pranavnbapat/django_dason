from fastapi import FastAPI
from app.api.metadata import meta_router
from app.api.object import object_router

app = FastAPI()

app.include_router(meta_router)
app.include_router(object_router)
