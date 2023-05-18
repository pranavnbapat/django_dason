from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import AdminMenuMixin, CustomPermissionRequiredMixin
from django.views.generic import TemplateView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import JsonResponse
from elasticsearch_dsl import Search
from elasticsearch_dsl.query import MoreLikeThis
from elasticsearch_dsl.connections import connections
import os
os.environ["ELASTIC_CLIENT_IGNORE_VERSION_CHECK"] = "true"
os.environ['ELASTIC_CLIENT_DISABLE_PRODUCT_CHECK'] = 'true'


class MoreLikeThisView(CustomPermissionRequiredMixin, UserPassesTestMixin, TemplateView, LoginRequiredMixin,
                       AdminMenuMixin):
    template_name = "backend/autocomplete/morelikethis.html"
    permission_menu = 'morelikethis'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        search_value = request.GET.get('search_value', '')
        print(search_value)
        es_client = connections.get_connection()

        if es_client.ping() and search_value:
            print("Using ES")

            s = Search(using=es_client, index="es_test_index")
            s = s.query(MoreLikeThis(like=search_value, fields=['title', 'content', 'author'], min_term_freq=1))
            s = s.source(exclude=["content"])
            s = s.extra(explain=True)
            print(s.to_dict())
            response = s.execute()
            print(response)

            # Extract the title, content and author values from the hits
            suggestions = [{'title': hit.title, 'author': hit.author} for hit in response]
            print(suggestions)
            return JsonResponse(suggestions, safe=False)

        return super().get(request, *args, **kwargs)
