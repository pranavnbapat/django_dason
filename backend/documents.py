from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from backend.models import FakerModel


@registry.register_document
class FakerModelDocument(Document):
    keywords = fields.TextField(attr='keywords')
    description = fields.TextField(attr='description')

    class Index:
        name = 'fakermodel'
        settings = {'number_of_shards': 1, 'number_of_replicas': 0}

    class Django:
        model = FakerModel
        fields = ['status', 'created_at', 'updated_at']
