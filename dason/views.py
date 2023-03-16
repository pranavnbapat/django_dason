from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from allauth.account.views import PasswordSetView, PasswordChangeView
from django_otp.plugins.otp_totp.models import TOTPDevice
import pandas as pd


# Dashboard
class DashboardView(LoginRequiredMixin, View):
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

    def get(self, request):
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

        return render(request, "backend/dashboard.html", context)


class Settings(LoginRequiredMixin, View):
    template_name = "backend/settings.html"

    def __init__(self, *args):
        super(Settings, self).__init__(*args)

    def get(self, request):
        k = TOTPDevice.objects.filter(user=request.user)
        context_data = {"k": k}
        return render(request, self.template_name, context_data)


class MyPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    success_url = reverse_lazy("dashboard")


class MyPasswordSetView(LoginRequiredMixin, PasswordSetView):
    success_url = reverse_lazy("dashboard")


def home(req):
    return render(req, "frontend/home.html")
