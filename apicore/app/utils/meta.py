from datetime import datetime
import pathlib
import hashlib


class KnowledgeObjectProperties(object):

    def __init__(self, knowledge_object):
        self.knowledge_object = knowledge_object

    def get_name(self):
        return self.knowledge_object.filename

    def get_extension(self):
        return pathlib.Path(self.knowledge_object.filename).suffix

    def get_size(self):
        return self.knowledge_object.file.tell()

    def get_object_hash(self):
        buf_size = 10_000_000
        md5 = hashlib.md5()

        self.knowledge_object.file.seek(0)
        while True:
            data = self.knowledge_object.file.read(buf_size)
            if not data:
                break
            md5.update(data)

        return md5.hexdigest()


def get_date_time():
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S.%f'")


def get_current_user():
    return 'test_user'


def create_object_metadata(ko):
    exec_time = get_date_time()

    return {
        "object_name": ko.get_name(),
        "object_hash": ko.get_object_hash(),
        "object_extension": ko.get_extension(),
        "object_size": ko.get_size(),
        "created_ts": exec_time,
        "created_by": get_current_user(),
        "updated_ts": exec_time,
        "updated_by": get_current_user(),
        "version": 1,
        "status": "new"

    }
