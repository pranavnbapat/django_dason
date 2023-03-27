from django.urls import path

from .views import (
    form_view,
    profile_view,
    dashboard_view,
    all_users_view,
    settings_view,
)

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
    path("settings", view=settings_view, name="settings")
]
