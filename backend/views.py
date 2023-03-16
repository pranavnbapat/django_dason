from django.contrib.auth import get_user_model
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required


class FormView(TemplateView):
    template_name = "backend/forms/form.html"


# Forms
form_view = login_required(FormView.as_view())
