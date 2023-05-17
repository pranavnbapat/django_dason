from django.views.generic.base import ContextMixin
from .context_processors import get_admin_menu
from django.contrib.auth.models import Permission
from django.shortcuts import redirect
from django.contrib.auth.mixins import UserPassesTestMixin
from backend.models import CustomPermissions, GroupCustomPermissions, PermissionMaster, AdminMenuMaster
from django.core.exceptions import ObjectDoesNotExist


class CustomPermissionRequiredMixin(UserPassesTestMixin):
    permission_menu = ''  # define this in your view

    def test_func(self):
        if self.request.user.is_superuser or self.request.user.is_staff:
            return True
        try:
            # Get the AdminMenuMaster instance for the relevant menu
            menu = AdminMenuMaster.objects.get(menu_route=self.permission_menu)
            # Get the PermissionMaster instance for 'can_view' action
            permission_master = PermissionMaster.objects.get(menu=menu, action='view')
        except ObjectDoesNotExist:
            return False

        # Check if the user has the permission
        has_permission = CustomPermissions.objects.filter(
            user=self.request.user, permission_name=permission_master
        ).exists()

        has_group_permission = GroupCustomPermissions.objects.filter(
            group__in=self.request.user.groups.all(), permission_names=permission_master
        ).exists()

        return has_permission or has_group_permission

    def handle_no_permission(self):
        return redirect('backend:dashboard')


class AdminMenuMixin(ContextMixin):
    def get_permissions(self, user):
        if user.is_authenticated:
            # Get user group
            groups = user.groups.all()

            # Get permission for group
            group_permissions = Permission.objects.filter(group__in=groups)

            # Get permissions for user
            user_permissions = user.user_permissions.all()

            # Combine group and user permissions
            permissions = group_permissions | user_permissions

            # Create a dictionary containing all permissions and their values
            permission_items = {
                f'{perm.codename}': True for perm in permissions
            }
        else:
            permission_items = {}
        print(permission_items)
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
