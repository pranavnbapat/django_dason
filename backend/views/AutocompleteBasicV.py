from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import AdminMenuMixin, CustomPermissionRequiredMixin
from django.views.generic import TemplateView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import JsonResponse
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search
from elasticsearch_dsl.query import MoreLikeThis, Prefix
from elasticsearch_dsl.connections import connections
import os
os.environ["ELASTIC_CLIENT_IGNORE_VERSION_CHECK"] = "true"
os.environ['ELASTIC_CLIENT_DISABLE_PRODUCT_CHECK'] = 'true'


class AutocompleteBasicView(CustomPermissionRequiredMixin, UserPassesTestMixin, TemplateView, LoginRequiredMixin, AdminMenuMixin):
    template_name = "backend/autocomplete/autocomplete-basic.html"
    permission_menu = 'autocomplete-basic'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        search_value = request.GET.get('search_value', '')
        # Check if Elasticsearch server is running
        es_client = connections.get_connection()

        if es_client.ping() and search_value:
            print("Using ES")
            # es = Elasticsearch(
            #     ['localhost'],
            #     http_auth=('elastic', 'asdasdasd'),
            #     scheme="https",
            #     port=443,
            #     verify_certs=False
            # )
            #
            # body = {
            #     "suggest": {
            #         "email_suggest": {
            #             "prefix": request.GET.get('search_value', ''),
            #             "completion": {
            #                 "field": "email_suggest"
            #             }
            #         }
            #     }
            # }

            # res = es.search(index='only_es_users_index', body=body)

            s = Search(using=es_client, index="only_es_users_index")
            # s = s.suggest('my_suggestion', search_value, term={'field': 'fname'})
            # s = s.query(MoreLikeThis(like=search_value, fields=['fname']))
            s = s.query(Prefix(fname=search_value))
            response = s.execute()
            print(response)

            # options = response.suggest.my_suggestion[0].options
            # suggestions = [option.text for option in options]
            # print(suggestions)
            #
            # return JsonResponse(suggestions, safe=False)

            suggestions = [{'fname': hit.fname, 'email': hit.email} for hit in response]  # Extract the fname and email values from the hits
            return JsonResponse(suggestions, safe=False)

        return super().get(request, *args, **kwargs)
