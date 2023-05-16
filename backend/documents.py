from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from backend.models import FakerModel, ESUsers, ESCityMaster, ESContactNo


@registry.register_document
class FakerModelDocument(Document):
    keywords = fields.TextField(attr='keywords')
    contact_no = fields.LongField(attr='contact_no')
    # keywords - This is a TextField, which means it will be indexed as a full-text searchable field.
    # The attr='keywords' part tells the document to use the keywords attribute of the FakerModel for this field.

    class Index:
        name = 'faker_model_index'
        settings = {'number_of_shards': 1, 'number_of_replicas': 0}
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
        model = FakerModel  # This tells the document class that it should be associated with the FakerModel model.

        # This is a list of fields from the FakerModel that should also be indexed. These fields will be indexed with
        # their default Elasticsearch field types. In this case, both fields are likely datetime fields.
        # fields = ['created_at', 'updated_at']


# @registry.register_document
# class ESCityMasterDocument(Document):
#     city_name = fields.KeywordField(attr='city_name')
#
#     class Index:
#         name = 'es_city_master_index'
#
#     class Django:
#         model = ESCityMaster


# @registry.register_document
# class ESUsersDocument(Document):
#     email = fields.KeywordField(attr='email')
#     dob = fields.DateField(attr='dob')
#     fname = fields.KeywordField(attr='fname')
#     lname = fields.KeywordField(attr='lname')
#     city_id = fields.IntegerField(attr='city_id')
#     city = fields.ObjectField(attr='city', properties={
#         'city_id': fields.IntegerField(),
#         'city_name': fields.KeywordField(),
#     })
#     contact_numbers = fields.NestedField(properties={
#         'contact_no': fields.LongField(),
#     })
#
#     class Index:
#         name = 'es_users_index'
#         settings = {'number_of_shards': 1, 'number_of_replicas': 0}
#
#     class Django:
#         model = ESUsers
#
#     def prepare_city(self, instance):
#         try:
#             city = ESCityMaster.objects.get(id=instance.city_id)
#             return {
#                 'city_id': city.id,
#                 'city_name': city.city_name,
#             }
#         except ESCityMaster.DoesNotExist:
#             return {}
#
#     def prepare_contact_numbers(self, instance):
#         return [{'contact_no': contact.contact_no} for contact in instance.escontactno_set.all()]


# @registry.register_document
# class ESContactNoDocument(Document):
#     es_users_id = fields.IntegerField(attr='es_users_id_id')
#     contact_no = fields.LongField(attr='contact_no')
#
#     class Index:
#         name = 'es_contact_no_index'
#
#     class Django:
#         model = ESContactNo


@registry.register_document
class ESUsersSingleDocument(Document):
    email = fields.KeywordField(attr='email')
    dob = fields.DateField(attr='dob')
    fname = fields.KeywordField(attr='fname')
    lname = fields.KeywordField(attr='lname')

    class Index:
        name = 'only_es_users_index'
        settings = {'number_of_shards': 1, 'number_of_replicas': 0}

    class Django:
        model = ESUsers
