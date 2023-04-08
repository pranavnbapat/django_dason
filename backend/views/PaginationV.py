from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import AdminMenuMixin, PermissionRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import TemplateView
from django.core.paginator import Paginator
from rest_framework.views import APIView
from rest_framework.response import Response
from backend.models import FakerModel
from backend.serializers import FakerModelSerializer
from django.http import JsonResponse
from django.db.models import Q
from django.db.models import F
from rest_framework import pagination
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser


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

        if search_value:
            queryset = FakerModel.objects.filter(
                Q(description__icontains=search_value) |
                Q(keywords__icontains=search_value)
            )
        else:
            queryset = FakerModel.objects.all()

        return queryset
