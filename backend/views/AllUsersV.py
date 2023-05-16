from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import AdminMenuMixin, PermissionRequiredMixin
from django.views.generic import ListView
from django.contrib.auth.mixins import UserPassesTestMixin
from backend.models import DefaultAuthUserExtend
from django.urls import resolve


class AllUsersView(PermissionRequiredMixin, UserPassesTestMixin, LoginRequiredMixin, ListView, AdminMenuMixin):
    template_name = "backend/user/all_users.html"
    permission_required = 'backend.view_users'
    context_object_name = 'all_users'
    model = DefaultAuthUserExtend

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.exclude(
            is_superuser=True,
            id=self.request.user.id
        ).prefetch_related('groups')

        return queryset

    def get_template_names(self):
        if resolve(self.request.path_info).url_name == 'users-grid':
            return ["backend/user/all-users-grid.html"]
        return super().get_template_names()
