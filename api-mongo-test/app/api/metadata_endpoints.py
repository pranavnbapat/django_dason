from fastapi import HTTPException, APIRouter
from pymongo.errors import PyMongoError
import json
from ..db.mongo import collection
from bson import ObjectId

meta_router = APIRouter()


class JSONEncoder(json.JSONEncoder):

    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)


@meta_router.get("/")
async def root():
    return {"message": "Fast API Is running"}


@meta_router.get("/get_all_items")
async def get_all_items():
    try:
        items = list(collection.find({}))
        return JSONEncoder().encode(items)
    except PyMongoError as e:
        raise HTTPException(status_code=500, detail=str(e))


@meta_router.get("/get_item/{item_id}")
async def get_item(item_id: str):
    try:
        item = collection.find_one({'_id': ObjectId(item_id)})
        if item:
            return JSONEncoder().encode(item)
        else:
            raise HTTPException(status_code=404, detail="Item not found")
    except PyMongoError as e:
        raise HTTPException(status_code=500, detail=str(e))


@meta_router.post("/add_item")
async def add_item(item: dict):
    try:
        collection.insert_one(item)
        return {"message": "Item added successfully"}
    except PyMongoError as e:
        raise HTTPException(status_code=500, detail=str(e))


@meta_router.put("/update_item/{item_id}")
async def update_item(item_id: str, item: dict):
    try:
        collection.update_one({'_id': item_id}, {'$set': item})
        return {"message": "Item updated successfully"}
    except PyMongoError as e:
        raise HTTPException(status_code=500, detail=str(e))


@meta_router.delete("/delete_item/{item_id}")
async def delete_item(item_id: str):
    try:
        collection.delete_one({'_id': ObjectId(item_id)})
        return {"message": "Item deleted successfully"}
    except PyMongoError as e:
        raise HTTPException(status_code=500, detail=str(e))
