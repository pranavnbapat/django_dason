from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from backend.models import FakerModel


@registry.register_document
class FakerModelDocument(Document):
    keywords = fields.TextField(attr='keywords')
    contact_no = fields.TextField(attr='contact_no')

    class Index:
        name = 'fakermodel'
        settings = {'number_of_shards': 5, 'number_of_replicas': 2}
        '''
        number_of_shards
        This setting determines how many primary shards the index should have. Shards are essentially smaller 
        partitions of the index, which allow Elasticsearch to distribute and parallelize operations across multiple 
        nodes.
        
        number_of_replicas
        This setting specifies the number of replica shards (copies) for each primary shard in the index. 
        Replica shards provide redundancy and allow Elasticsearch to distribute search load across nodes.
        '''

    class Django:
        model = FakerModel
        fields = ['created_at', 'updated_at']
