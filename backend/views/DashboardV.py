from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import AdminMenuMixin
from django.views.generic import TemplateView
from .data_processing import process_dashboard_data


class DashboardView(LoginRequiredMixin, TemplateView, AdminMenuMixin):
    template_name = "backend/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = process_dashboard_data()
        context.update(data)
        return context

    # Another way of writing this class is below. Include View instead of TemplateView and don't write template_name
    # def get(self, request, *args, **kwargs):
    #     data = process_dashboard_data()
    #
    #     custom_context = self.get_context_data(**data)
    #     context = {**data, **custom_context}
    #
    #     return render(request, "backend/dashboard.html", context)
