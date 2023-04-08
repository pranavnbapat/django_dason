from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import AdminMenuMixin, PermissionRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import TemplateView
from django.core.paginator import Paginator
from rest_framework.views import APIView
from rest_framework.response import Response
# from backend.models import User
# from backend.serializers import UserSerializer


class PaginationView(PermissionRequiredMixin, UserPassesTestMixin, LoginRequiredMixin, AdminMenuMixin, TemplateView):
    template_name = "backend/pagination/pagination.html"
    permission_required = 'backend_viewpagination'


# class UserPaginationAPIView(APIView):
#     def get(self, request, *args, **kwargs):
#         page = request.GET.get('page', 1)
#         limit = request.GET.get('limit', 10)
#
#         users = User.objects.all()
#         paginator = Paginator(users, limit)
#
#         user_data = paginator.get_page(page)
#         serializer = UserSerializer(user_data, many=True)
#
#         response_data = {
#             'recordsTotal': users.count(),
#             'recordsFiltered': users.count(),
#             'data': serializer.data,
#         }
#
#         return Response(response_data)
