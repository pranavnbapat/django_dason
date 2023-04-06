from django.views.generic.base import ContextMixin
from .context_processors import get_admin_menu
from django.contrib.auth.models import Permission
from django.shortcuts import redirect
from django.contrib.auth.mixins import UserPassesTestMixin


class AdminMenuMixin(ContextMixin):
    def get_permissions(self, user):
        if user.is_authenticated:
            # Get user group
            groups = user.groups.all()

            # Get permission for group
            permissions = Permission.objects.filter(group__in=groups)

            # Create a dictionary containing all permissions and their values
            permission_items = {
                f'can_{perm.codename}': True for perm in permissions
            }
        else:
            permission_items = {}

        context = {"permissions": permission_items}

        return context

    def get_admin_menu(self):
        context = get_admin_menu()
        return context

    def get_context_data(self, **kwargs):
        if hasattr(super(), 'get_context_data'):
            context = super().get_context_data(**kwargs)
        else:
            context = kwargs

        context.update(self.get_admin_menu())
        context.update(self.get_permissions(self.request.user))

        return context


class PermissionRequiredMixin(UserPassesTestMixin):
    permission_required = None

    def test_func(self):
        user = self.request.user
        if user.is_superuser:
            return True

        if self.permission_required and user.has_perm(self.permission_required):
            return True

        return False

    def handle_no_permission(self):
        return redirect('backend:dashboard')
