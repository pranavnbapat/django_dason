from django.urls import path
from .views import (
    form_view,
    profile_view,
    dashboard_view,
    all_users_view,
    fastapi_test_view,
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
    path("users-grid", view=all_users_view, name="users-grid"),

    path("fastapi-test/", view=fastapi_test_view, name="fastapi-test")
]
