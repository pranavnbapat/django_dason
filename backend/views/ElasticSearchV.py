from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .mixins import AdminMenuMixin, PermissionRequiredMixin
from django.views.generic import TemplateView
from django.http import JsonResponse
from backend.documents import ESUsersDocument, ESCityMasterDocument
from elasticsearch_dsl.connections import connections
from backend.models import ESUsers
from django.db.models import Q
from datetime import datetime


def is_valid_date(date_string, date_format='%Y-%m-%d'):
    try:
        datetime.strptime(date_string, date_format)
        return True
    except ValueError:
        return False


class ElasticSearchView(PermissionRequiredMixin, UserPassesTestMixin, LoginRequiredMixin, AdminMenuMixin, TemplateView):
    template_name = 'backend/elastic_search/elastic-search.html'
    permission_required = 'backend_viewelasticsearch'


class ElasticSearchResultsView(PermissionRequiredMixin, UserPassesTestMixin, LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        search_value = request.GET.get('search_value', '')

        # Check if Elasticsearch server is running
        es_client = connections.get_connection()
        response_data = []
        if es_client.ping() and search_value:
            print("Using Elasticsearch")

            should_clauses = [
                {"match": {"email": {"query": search_value, "boost": 10}}},
                {"match": {"fname": {"query": search_value, "boost": 5}}},
                {"match": {"lname": {"query": search_value, "boost": 5}}},
                {"nested": {
                    "path": "contact_numbers",
                    "query": {"match": {"contact_numbers.contact_no": search_value}}
                }},
                {"nested": {
                    "path": "city",
                    "query": {"match": {"city.city_name": search_value}}
                }},
            ]

            # if is_valid_date(search_value):
            #     should_clauses += [
            #         {"match_phrase": {"dob": {"query": search_value, "boost": 2}}},
            #         {"match": {"dob": search_value}},
            #     ]

            # if is_valid_date(search_value):
            #     search_date = datetime.strptime(search_value, '%Y-%m-%d').date()
            #     search_date = datetime.combine(search_date, datetime.min.time())
            #     should_clauses += [
            #         {
            #             "script": {
            #                 "script": f"doc['dob'].value.toInstant().toEpochMilli() == {int(search_date.timestamp())} * 1000"
            #             }
            #         },
            #     ]

            # if search_value.isdigit():
            #     should_clauses += [
            #         {"nested": {
            #             "path": "contact_numbers",
            #             "query": {"match": {"contact_numbers.contact_no": search_value}}
            #         }},
            #     ]

            search = ESUsersDocument.search().query(
                'bool',
                should=should_clauses,
                minimum_should_match=1
            )

            for hit in search:
                response_data.append({
                    'id': hit.meta.id,
                    'email': hit.email,
                    'dob': hit.dob,
                    'fname': hit.fname,
                    'lname': hit.lname,
                    'city': hit.city['city_name'],
                    'contact_numbers': [num.contact_no for num in hit.contact_numbers],
                })
        else:
            print("Using default search method")
            if search_value:
                search = ESUsers.objects.filter(
                    Q(email__icontains=search_value) |
                    Q(fname__icontains=search_value) |
                    Q(lname__icontains=search_value) |
                    Q(dob__icontains=search_value)
                ).select_related("es_city_master")
            else:
                search = ESUsers.objects.all()
            for hit in search:
                contact_numbers = [contact.contact_no for contact in hit.contact_numbers]
                response_data.append({
                    'id': hit.id,
                    'email': hit.email,
                    'dob': hit.dob,
                    'fname': hit.fname,
                    'lname': hit.lname,
                    'city': hit.city_master.city_name,
                    'contact_numbers': contact_numbers,
                })

        return JsonResponse(response_data, safe=False)
