import pandas as pd
import os
import random
import string
from django.conf import settings


def generate_random_filename(length: int):
    """Generate a random alphanumeric filename with the specified length."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


def process_dashboard_data():
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

    data = {'devices': list(df_users_devices['Device']), 'users': list(df_users_devices['Users'])}
    data_users_over_period = {'date': list(df_users_over_period['Date']),
                              'users': list(df_users_over_period['Users'])}
    data_new_ret_vis = {'user_type': list(df_new_ret_vis['User Type']),
                        'sessions': list(df_new_ret_vis['Sessions'])}
    data_lang_spec_new_ret_vis = {'lang': list(df_lang_spec_new_ret_vis['Language']),
                                  'users': list(df_lang_spec_new_ret_vis['Users']),
                                  'new_users': list(df_lang_spec_new_ret_vis['New Users'])}
    data_top_acq_channels = {'channel': list(df_top_acq_channels['Default Channel Grouping']),
                             'users': list(df_top_acq_channels['Users'])}
    data_new_ret_users_timeseries = {'date': list(df_new_ret_users_timeseries['Date']),
                                     'users': list(df_new_ret_users_timeseries['Users']),
                                     'new_users': list(df_new_ret_users_timeseries['New Users'])}
    data_page_popularity = {'page': list(df_page_popularity['Page']),
                            'pageviews': list(df_page_popularity['Pageviews'])}

    return {
        'data_json': data,
        'data_users_over_period': data_users_over_period,
        'data_new_ret_vis': data_new_ret_vis,
        'data_lang_spec_new_ret_vis': data_lang_spec_new_ret_vis,
        'data_top_acq_channels': data_top_acq_channels,
        'data_new_ret_users_timeseries': data_new_ret_users_timeseries,
        'data_page_popularity': data_page_popularity,
    }


def manage_avatar_upload(file, len=20):
    os.makedirs(settings.AVATAR_PATH, exist_ok=True)
    random_filename = generate_random_filename(len)
    _, file_ext = os.path.splitext(file.name)
    avatar = random_filename + file_ext

    with open(os.path.join(settings.AVATAR_PATH, avatar), 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

    return avatar
