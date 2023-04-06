from django.urls import path
from .views import (
    FormView,
    ProfileView,
    DashboardView,
    AllUsersView,
    KOView,
)
from django.contrib.auth.decorators import login_required

app_name = "backend"

urlpatterns = [
    path("my-form/", view=FormView.as_view(), name="my-form"),
    # path("my_form/submit/", view=form_view, name="my_form_submit"),

    path("user/profile", view=ProfileView.as_view(), name="user.profile"),

    # Dashboard
    path('dashboard/', view=DashboardView.as_view(), name="dashboard"),

    # Users
    path("users", view=AllUsersView.as_view(), name="users"),
    path("users-grid", view=AllUsersView.as_view(), name="users-grid"),

    # Knowledge Objects
    path("knowledge-objects", view=KOView.as_view(), name="knowledge-objects"),

    # FastAPI View
    path("fastapi-view", view=KOView.as_view(), name="fastapi-view"),
]
