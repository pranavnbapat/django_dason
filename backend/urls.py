from django.urls import path
from backend import views
from .views import (
    form_view,
    profile_view,
    dashboard_view,
    all_users_view,
    settings_view,
)
from django.contrib.auth.decorators import login_required

app_name = "backend"

urlpatterns = [
    path("my_form/", view=form_view, name="my_form"),
    # path("my_form/submit/", view=form_view, name="my_form_submit"),

    path("user/profile", view=profile_view, name="user.profile"),

    # Dashboard
    path('dashboard/', view=dashboard_view, name="dashboard"),

    # Users
    path("users", view=all_users_view, name="users"),

    # Settings
    path("settings", view=settings_view, name="settings"),

    path(
        "account/password/change/",
        login_required(views.MyPasswordChangeView.as_view()),
        name="account_change_password",
    ),
    # Custom set password done page redirect
    path(
        "account/password/set/",
        login_required(views.MyPasswordSetView.as_view()),
        name="account_set_password",
    ),
]
