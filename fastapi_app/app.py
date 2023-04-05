from fastapi import FastAPI

app = FastAPI()

@app.get("/backend/fastapi/test/")
def read_root():
    return {"Hello": "from FastAPI"}
