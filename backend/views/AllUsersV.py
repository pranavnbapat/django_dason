from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import AdminMenuMixin, PermissionRequiredMixin
from django.views.generic import ListView
from django.shortcuts import redirect
from django.contrib.auth.mixins import UserPassesTestMixin
from ..models import DefaultAuthUserExtend


class AllUsersView(PermissionRequiredMixin, UserPassesTestMixin, LoginRequiredMixin, ListView, AdminMenuMixin):
    template_name = "backend/user/all_users.html"
    permission_required = 'backend.view_users'
    context_object_name = 'all_users'
    model = DefaultAuthUserExtend

    def test_func(self):
        user = self.request.user
        if user.is_superuser or user.has_perm('backend.view_users'):
            return True
        return False

    def handle_no_permission(self):
        return redirect('backend:dashboard')

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.exclude(
            is_superuser=True,
            id=self.request.user.id
        ).prefetch_related('groups')

        return queryset

    def get_template_names(self):
        if self.request.path == '/backend/users-grid':
            return ["backend/user/all-users-grid.html"]
        return super().get_template_names()
