import datetime
from fastapi import APIRouter, UploadFile
import time
from ..db.minio import upload, check_if_object_exists
from .metadata import add_item
from ..utils.meta import KnowledgeObjectProperties, create_object_metadata

object_router = APIRouter(
    prefix="/object",
    tags=["object"]
)


@object_router.get("/")
def root():
    return "hello world"


@object_router.post("/upload")
async def upload_file(ufile: UploadFile):
    ko = KnowledgeObjectProperties(ufile)
    t = time.time()
    filename_hash = ko.get_object_hash()

    if not check_if_object_exists(filename_hash):

        upload(ufile, filename=filename_hash)
        await add_item(create_object_metadata(ko))
        return f"Successfully uploaded {ko.get_name()} with hash {ko.get_object_hash()} in {time.time() - t}"

    else:
        return f"Not Uploaded. {ko.get_name()} with hash {ko.get_object_hash()} already exists in {time.time() - t}"
