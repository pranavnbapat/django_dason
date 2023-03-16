from django.urls import path

from .views import (
    form_view
)

app_name = "backend"

urlpatterns = [
    path(
        "forms/form",
        view=form_view,
        name="form"
    )
]
