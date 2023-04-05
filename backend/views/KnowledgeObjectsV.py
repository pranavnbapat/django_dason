from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import AdminMenuMixin
from django.views.generic import TemplateView
import os
from django.conf import settings
from .data_processing import nested_list_to_csv
from django.db import connections


class KOView(TemplateView, LoginRequiredMixin, AdminMenuMixin):
    template_name = "backend/ko/knowledge_objects.html"

    @staticmethod
    def get_mongodb_data():
        client = settings.MONGO_CLIENT
        db = client[os.getenv("MONGODB_DB")]
        collection = db['knowledge_objects']

        data = collection.find({})
        return list(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mongodb_data = self.get_mongodb_data()
        context['ko'] = mongodb_data
        context['array_to_csv'] = nested_list_to_csv

        with connections['default'].cursor() as cursor:
            cursor.execute('SELECT * FROM admin_menu_master')
            all_users = cursor.fetchall()

        context.update({'all_users': all_users})

        return context
