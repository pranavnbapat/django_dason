from fastapi import FastAPI
from app.api.metadata_endpoints import meta_router

app = FastAPI()

app.include_router(meta_router)

