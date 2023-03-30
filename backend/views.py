from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from .context_processors import get_admin_menu, get_countries
from .forms import MyFormForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.db import connections
from django.views.generic.base import ContextMixin
from .data_processing import process_dashboard_data, manage_avatar_upload


class AdminMenuMixin(ContextMixin):
    def get_admin_menu(self):
        context = get_admin_menu()
        return context

    def get_context_data(self, **kwargs):
        if hasattr(super(), 'get_context_data'):
            context = super().get_context_data(**kwargs)
        else:
            context = kwargs
        context.update(self.get_admin_menu())
        return context


class FormView(LoginRequiredMixin, TemplateView, AdminMenuMixin):
    template_name = "backend/forms/form.html"

    def get(self, request, *args, **kwargs):
        form = MyFormForm()
        context = self.get_context_data(form=form)
        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_countries())
        return context

    def post(self, request):
        form = MyFormForm(request.POST, request.FILES)

        if form.is_valid():
            form_data = form.save(commit=False)

            if request.FILES['avatar']:
                file = request.FILES['avatar']
                avatar = manage_avatar_upload(file)
                form_data.avatar = avatar

            form_data.save()
            messages.success(request, "Form data saved successfully.")
            return redirect('backend:my_form')
        else:
            messages.error(request, "There was an error processing the form.")
            context = self.get_context_data(form=form)
            return render(request, self.template_name, context)


class ProfileView(LoginRequiredMixin, TemplateView, AdminMenuMixin):
    template_name = "backend/user/profile.html"


class DashboardView(LoginRequiredMixin, View, AdminMenuMixin):
    def get(self, request, *args, **kwargs):
        data = process_dashboard_data()

        custom_context = self.get_context_data(**data)
        context = {**data, **custom_context}

        return render(request, "backend/dashboard.html", context)


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


# Forms
form_view = login_required(FormView.as_view())

# User profile
profile_view = login_required(ProfileView.as_view())

# Dashboard
dashboard_view = login_required(DashboardView.as_view())

# All users
all_users_view = login_required(AllUsersView.as_view())

