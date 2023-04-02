from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import AdminMenuMixin
from django.views.generic import TemplateView
from django.db import connections
from django.shortcuts import render


class AllUsersView(LoginRequiredMixin, TemplateView, AdminMenuMixin):
    template_name = "backend/user/all_users.html"

    def get(self, request, *args, **kwargs):
        current_user_id = self.request.user.id

        with connections['default'].cursor() as cursor:
            cursor.execute('SELECT au.first_name, au.last_name, au.username, au.email, au.last_login, au.is_staff, '
                           'ag.name as group_name, au.is_active, au.date_joined, au.id '
                           'FROM auth_user au '
                           'LEFT JOIN auth_user_groups aug ON au.id = aug.user_id '
                           'LEFT JOIN auth_group ag ON ag.id = aug.group_id '
                           'WHERE au.is_superuser != 1 AND au.id != ' + str(current_user_id))
            all_users = cursor.fetchall()
        context = {'all_users': all_users}

        print(request.path)
        if request.path == '/backend/users-grid':
            self.template_name = "backend/user/all-users-grid.html"

        custom_context = self.get_context_data(context=context)
        context.update(custom_context)

        return render(request, self.template_name, context)
