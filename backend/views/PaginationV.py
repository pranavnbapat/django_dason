from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import AdminMenuMixin, PermissionRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import TemplateView
from backend.models import FakerModel
from backend.serializers import FakerModelSerializer
from django.http import JsonResponse
from backend.documents import FakerModelDocument
from rest_framework import pagination
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from elasticsearch_dsl.connections import connections


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
            # By default, elastic search performs OR operation if more than one search parameter is passed.

            # Use Elasticsearch to perform the search in multiple columns
            search = FakerModelDocument.search().query(
                'multi_match',
                query=search_value,
                fields=['keywords', 'description']
            )

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
