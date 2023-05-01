from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .mixins import AdminMenuMixin, PermissionRequiredMixin
from django.views.generic import TemplateView
from backend.models import FakerModel, ElasticSearchStatistics
from backend.serializers import FakerModelSerializer
from django.http import JsonResponse, HttpResponse
from backend.documents import FakerModelDocument
from rest_framework import pagination
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q, F
from elasticsearch_dsl import Search, Q
from elasticsearch_dsl.connections import connections
from django.views import View
from django.urls import reverse


class PaginationView(PermissionRequiredMixin, UserPassesTestMixin, LoginRequiredMixin, AdminMenuMixin, TemplateView):
    template_name = "backend/pagination/pagination.html"
    permission_required = 'backend_viewpagination'


class CustomPagination(pagination.PageNumberPagination):
    page_size_query_param = 'length'
    page_query_param = 'start'

    def paginate_queryset(self, queryset, request, view=None):
        self.request = request
        page_size = self.get_page_size(request)
        if not page_size:
            return None

        start = int(request.GET.get('start', 0))
        page_number = start // page_size + 1

        paginator = self.django_paginator_class(queryset, page_size)
        self.page = paginator.page(page_number)
        self.is_paginated = True
        return list(self.page)

    def get_paginated_response(self, data):
        for item in data:
            item['contact_url'] = reverse('backend:record-click', args=[item['contact_no']])

        return JsonResponse({
            'draw': int(self.request.GET.get('draw', 0)),
            'recordsTotal': self.page.paginator.count,
            'recordsFiltered': self.page.paginator.count,
            'data': data,
        })


class PaginationAPI(ListAPIView):
    serializer_class = FakerModelSerializer
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        search_value = self.request.GET.get('search[value]', '')

        # Check if Elasticsearch server is running
        es_client = connections.get_connection()
        if es_client.ping() and search_value:
            print("Using Elasticsearch")
            search_terms = search_value.split()

            # NEW CODE
            # Update hit counts
            # for term in search_terms:
            #     for field in ['keywords', 'contact_no']:
            #         hit, created = ElasticSearchStatistics.objects.get_or_create(search_term=term, column_name=field)
            #         hit.hits = F('hits') + 1
            #         hit.save()

            # Prepare hit-based priority weights
            hit_weights = []
            for term in search_terms:
                for field in ['keywords', 'contact_no']:
                    hit = ElasticSearchStatistics.objects.filter(search_term=term, column_name=field).first()
                    if hit:
                        hit_weights.append((term, field, hit.hits))

            # Prepare search query with weights
            '''
            The code below constructs a function_score query based on the hit-based priority weights. 
            It creates a query object and adds a subquery for each term, field, and weight combination. 
            The function_score query is used to modify the score of documents returned by the subqueries, 
            making it possible to prioritize certain documents based on the hit weights.
            '''

            # search = Search(index=FakerModelDocument._index._name)
            # query = Q()
            #
            # for term, field, weight in hit_weights:
            #     query |= Q('nested', path=field,
            #                query=Q('match', **{f"{field}.search_term": {"query": term, "boost": weight}}))
            #
            # search = search.query('function_score', query=query, score_mode='sum')

            '''
            The code below constructs a simple multi_match query. It searches for the search_value across the specified 
            fields (keywords and contact_no). This query does not consider hit-based priority weights and is a more 
            straightforward search query.
            '''
            # search = FakerModelDocument.search().query(
            #     'multi_match',
            #     query=search_value,
            #     fields=['keywords', 'contact_no']
            # )

            '''
            The below code is a combination of the first and second snippets. It constructs a function_score query 
            that uses a multi_match query inside. This approach allows you to search for the search_value across the 
            specified fields while still considering the hit-based priority weights. However, this might return less 
            relevant results if the hit counts are not well balanced.
            '''

            # search = Search(index=FakerModelDocument._index._name)
            # query = Q()
            #
            # for term, field, weight in hit_weights:
            #     query |= Q('nested', path=field,
            #                query=Q('match', **{f"{field}.search_term": {"query": term, "boost": weight}}))
            #
            # search = search.query('function_score',
            #                       query=Q('multi_match', query=search_value, fields=['keywords', 'contact_no']),
            #                       score_mode='sum')

            search = Search(index=FakerModelDocument._index._name)
            query = Q()

            for term, field, weight in hit_weights:
                # query |= Q('match', **{field: {"query": term, "boost": weight}})
                query |= Q('bool', should=[Q('match', **{field: {"query": term, "boost": weight}})])

            search = search.query('function_score', query=query, score_mode='sum')

            # NEW CODE

            # By default, elastic search performs OR operation if more than one search parameter is passed,
            # because the default behavior of Elasticsearch is to score the relevance of documents based on the number
            # of matching terms in the query string.

            # Use Elasticsearch to perform the search in multiple columns
            # search = FakerModelDocument.search().query(
            #     'multi_match',
            #     query=search_value,
            #     fields=['keywords', 'contact_no']
            # )

            # Code below searches for records using AND operation
            # Split the search_value into individual terms

            # search = FakerModelDocument.search().query(
            #     'bool',
            #     must=[
            #         {
            #             'multi_match': {
            #                 'query': term,
            #                 'fields': ['keywords', 'contact_no']
            #             }
            #         }
            #         for term in search_terms
            #     ]
            # )
            # To retrieve more records, append this to the search above
            # .extra(size=1000)  # Increase the size to get more results
            # By default, it gives only 10 results

            # Search in only one column (e.g., keywords)
            # search = FakerModelDocument.search().query(
            #     'match',
            #     keywords=search_value
            # )

            # Search with a preference for keywords, and then in description if not found in keywords:
            # search = FakerModelDocument.search().query(
            #     'bool',
            #     should=[
            #         {"match": {"keywords": {"query": search_value, "boost": 2}}},
            #         {"match": {"description": search_value}},
            #     ],
            #     minimum_should_match=1
            # )
            ids = [hit.meta.id for hit in search]
            queryset = FakerModel.objects.filter(id__in=ids)
        else:
            print("Using default search method")
            # Fall back to default search method
            if search_value:
                queryset = FakerModel.objects.filter(
                    Q(description__icontains=search_value) |
                    Q(keywords__icontains=search_value)
                )
            else:
                queryset = FakerModel.objects.all()

        return queryset


class RecordClickView(View):
    def get(self, request, *args, **kwargs):
        result_id = request.GET.get('result_id')
        search_term = request.GET.get('search_term')
        column_name = request.GET.get('column_name')

        search_terms = search_term.split()
        for term in search_terms:
            hit, created = ElasticSearchStatistics.objects.get_or_create(search_term=term, column_name='keywords')
            hit.hits = F('hits') + 1
            hit.save()

        hit, created = ElasticSearchStatistics.objects.get_or_create(search_term=result_id, column_name='contact_no')
        hit.hits = F('hits') + 1
        hit.save()

        return HttpResponse(status=204)


class ShowPaginationContactView(PermissionRequiredMixin, UserPassesTestMixin, LoginRequiredMixin, AdminMenuMixin, TemplateView):
    template_name = "backend/pagination/contact_detail.html"
    permission_required = 'backend_viewcontactdetail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact_no'] = self.kwargs['contact_no']
        return context
