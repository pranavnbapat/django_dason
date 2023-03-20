from django.urls import path

from .views import (
    form_view,
    profile_view
)

app_name = "backend"

urlpatterns = [
    path("my_form/", view=form_view, name="my_form"),
    path("my_form/submit/", view=form_view, name="my_form_submit"),

    path("user/profile", view=profile_view, name="user.profile"),
]
