from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import AdminMenuMixin
from django.views.generic import TemplateView


class ProfileView(LoginRequiredMixin, TemplateView, AdminMenuMixin):
    template_name = "backend/user/profile.html"

