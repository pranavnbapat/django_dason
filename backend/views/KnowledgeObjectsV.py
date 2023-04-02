from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import AdminMenuMixin
from django.views.generic import TemplateView


class KOView(TemplateView, LoginRequiredMixin, AdminMenuMixin):
    template_name = "backend/ko/knowledge_objects.html"

