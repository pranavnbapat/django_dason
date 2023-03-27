from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from django.conf import settings
import os
import string
import random
from .context_processors import get_admin_menu
from .context_processors import greeting
from .forms import MyFormForm
import pandas as pd
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.urls import reverse_lazy
from allauth.account.views import PasswordSetView, PasswordChangeView
from django_otp.plugins.otp_totp.models import TOTPDevice
from django.db import connections
from django.views.generic.base import ContextMixin


def generate_random_filename(length: int):
    """Generate a random alphanumeric filename with the specified length."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


class AdminMenuMixin(ContextMixin):
    def get_admin_menu(self):
        custom_context = get_admin_menu()
        return custom_context

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

        custom_context = greeting(request)
        context = self.get_context_data(form=form)
        context.update(custom_context)

        return render(request, self.template_name, context)

    def post(self, request):
        form = MyFormForm(request.POST, request.FILES)

        if form.is_valid():
            form_data = form.save(commit=False)

            if form_data.avatar:
                file = request.FILES['avatar']
                # Ensure the AVATAR_PATH exists
                os.makedirs(settings.AVATAR_PATH, exist_ok=True)

                # Generate a random alphanumeric filename
                random_filename = generate_random_filename(length=20)

                # Remove the extension of the file and store it
                _, file_ext = os.path.splitext(file.name)

                avatar = random_filename + file_ext

                with open(os.path.join(settings.AVATAR_PATH, avatar), 'wb+') as destination:
                    for chunk in file.chunks():
                        destination.write(chunk)

            form_data.save()
            messages.success(request, "Form data saved successfully.")
            return redirect('backend:my_form')
        else:
            messages.error(request, "There was an error processing the form.")
            return render(request, 'backend/forms/form.html', {'form': form})


class ProfileView(LoginRequiredMixin, TemplateView, AdminMenuMixin):
    template_name = "backend/user/profile.html"


class DashboardView(LoginRequiredMixin, View, AdminMenuMixin):
    df_users_devices = pd.read_csv("data/analytics/device_specific_visitors.csv")

    df_users_over_period = pd.read_csv("data/analytics/users_visiting_over_year.csv")
    df_users_over_period['Date'] = pd.to_datetime(df_users_over_period['Date'], format='%b %d, %Y')
    df_users_over_period = df_users_over_period.groupby(pd.Grouper(key='Date', freq='M')).sum()
    df_users_over_period = df_users_over_period.reset_index()
    df_users_over_period['Date'] = df_users_over_period['Date'].dt.strftime('%b %Y')

    df_new_ret_vis = pd.read_csv("data/analytics/new_ret_users.csv")

    df_lang_spec_new_ret_vis = pd.read_csv("data/analytics/lang_specific_new_ret_users.csv")
    df_lang_spec_new_ret_vis = df_lang_spec_new_ret_vis.head(20)

    df_top_acq_channels = pd.read_csv("data/analytics/top_acq_channels.csv")

    df_new_ret_users_timeseries = pd.read_csv("data/analytics/new_ret_users_timeseries.csv")
    df_new_ret_users_timeseries['Date'] = pd.to_datetime(df_new_ret_users_timeseries['Date'], format='%b %d, %Y')
    df_new_ret_users_timeseries = df_new_ret_users_timeseries.groupby(pd.Grouper(key='Date', freq='M')).sum()
    df_new_ret_users_timeseries = df_new_ret_users_timeseries.reset_index()
    df_new_ret_users_timeseries['Date'] = df_new_ret_users_timeseries['Date'].dt.strftime('%b %Y')

    df_page_popularity = pd.read_csv("data/analytics/page_popularity.csv")
    df_page_popularity = df_page_popularity.head(10)

    def get(self, request, *args, **kwargs):
        data = {'devices': list(self.df_users_devices['Device']), 'users': list(self.df_users_devices['Users'])}
        data_users_over_period = {'date': list(self.df_users_over_period['Date']),
                                  'users': list(self.df_users_over_period['Users'])}
        data_new_ret_vis = {'user_type': list(self.df_new_ret_vis['User Type']),
                            'sessions': list(self.df_new_ret_vis['Sessions'])}
        data_lang_spec_new_ret_vis = {'lang': list(self.df_lang_spec_new_ret_vis['Language']),
                                      'users': list(self.df_lang_spec_new_ret_vis['Users']),
                                      'new_users': list(self.df_lang_spec_new_ret_vis['New Users'])}
        data_top_acq_channels = {'channel': list(self.df_top_acq_channels['Default Channel Grouping']),
                                 'users': list(self.df_top_acq_channels['Users'])}
        data_new_ret_users_timeseries = {'date': list(self.df_new_ret_users_timeseries['Date']),
                                         'users': list(self.df_new_ret_users_timeseries['Users']),
                                         'new_users': list(self.df_new_ret_users_timeseries['New Users'])}
        data_page_popularity = {'page': list(self.df_page_popularity['Page']),
                                'pageviews': list(self.df_page_popularity['Pageviews'])}

        context = {'data_json': data,
                   'data_users_over_period': data_users_over_period,
                   'data_new_ret_vis': data_new_ret_vis,
                   'data_lang_spec_new_ret_vis': data_lang_spec_new_ret_vis,
                   'data_top_acq_channels': data_top_acq_channels,
                   'data_new_ret_users_timeseries': data_new_ret_users_timeseries,
                   'data_page_popularity': data_page_popularity}

        custom_context = self.get_context_data(context=context)
        context.update(custom_context)

        return render(request, "backend/dashboard.html", context)


class SettingsView(LoginRequiredMixin, TemplateView, AdminMenuMixin):
    template_name = "backend/settings.html"

    def __init__(self, *args):
        super(SettingsView, self).__init__(*args)

    def get(self, request, *args, **kwargs):
        k = TOTPDevice.objects.filter(user=request.user)
        context = {"k": k}

        custom_context = self.get_context_data(context=context)
        context.update(custom_context)

        return render(request, self.template_name, context)

    def post(self, request):
        pass


class MyPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    success_url = reverse_lazy("dashboard")


class MyPasswordSetView(LoginRequiredMixin, PasswordSetView):
    success_url = reverse_lazy("dashboard")


class AllUsersView(LoginRequiredMixin, TemplateView, AdminMenuMixin):
    template_name = "backend/user/all_users.html"

    def get(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_user_id = self.request.user.id

        with connections['default'].cursor() as cursor:
            cursor.execute('SELECT au.first_name, au.last_name, au.username, au.email, au.last_login, au.is_staff, '
                           'ag.name as group_name, au.is_active, au.date_joined, au.id '
                           'FROM auth_user au '
                           'INNER JOIN auth_user_groups aug ON au.id = aug.user_id '
                           'INNER JOIN auth_group ag ON ag.id = aug.group_id '
                           'WHERE au.is_superuser != 1 AND au.id != ' + str(current_user_id))
            all_users = cursor.fetchall()
        context['all_users'] = all_users

        return context


# Forms
form_view = login_required(FormView.as_view())

# User profile
profile_view = login_required(ProfileView.as_view())

dashboard_view = login_required(DashboardView.as_view())

all_users_view = login_required(AllUsersView.as_view())

settings_view = login_required(SettingsView.as_view())
