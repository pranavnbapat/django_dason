from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .mixins import AdminMenuMixin
from django.shortcuts import render
from .data_processing import process_dashboard_data


class DashboardView(LoginRequiredMixin, View, AdminMenuMixin):
    def get(self, request, *args, **kwargs):
        data = process_dashboard_data()

        custom_context = self.get_context_data(**data)
        context = {**data, **custom_context}

        return render(request, "backend/dashboard.html", context)


# Dashboard
# dashboard_view = login_required(DashboardView.as_view())
