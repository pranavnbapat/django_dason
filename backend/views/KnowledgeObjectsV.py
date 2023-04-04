from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import AdminMenuMixin
from django.views.generic import TemplateView
from pymongo import MongoClient
from django.conf import settings
import os


def get_mongodb_data():
    client = settings.mongo_client
    db = client[os.getenv("MONGODB_DB")]  # Replace 'os.getenv("MONGODB_DB")' with your MongoDB database name
    collection = db['collection_name']  # Replace 'collection_name' with the collection you want to fetch data from

    data = collection.find({})  # Fetch all documents in the collection
    return list(data)


class KOView(TemplateView, LoginRequiredMixin, AdminMenuMixin):
    template_name = "backend/ko/knowledge_objects.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mongodb_data = get_mongodb_data()
        context['mongodb_data'] = mongodb_data
        return context
