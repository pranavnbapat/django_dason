from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views import View
from django.views.generic.base import ContextMixin
from backend.views.context_processors import get_admin_menu
from django.urls import reverse_lazy
from allauth.account.views import PasswordSetView, PasswordChangeView
from django_otp.plugins.otp_totp.models import TOTPDevice
from backend.urls import urlpatterns as backend_urlpatterns

def home(req):
    return render(req, "frontend/home.html")


class AdminMenuMixin(ContextMixin):
    def get_admin_menu(self):
        custom_context = get_admin_menu()
        return custom_context

    def get_context_data(self, **kwargs):
        if hasattr(super(), 'get_context_data'):
            context = super().get_context_data(**kwargs)
        else:
            context = kwargs
        context.update(self.get_admin_menu())
        return context


class Settings(LoginRequiredMixin, View, AdminMenuMixin):
    template_name = "backend/settings.html"

    def __init__(self, *args):
        super(Settings, self).__init__(*args)

    def get(self, request):
        k = TOTPDevice.objects.filter(user=request.user)
        context = {"k": k}

        custom_context = self.get_context_data(context=context)
        context.update(custom_context)

        return render(request, self.template_name, context)


class MyPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    success_url = reverse_lazy("dashboard")


class MyPasswordSetView(LoginRequiredMixin, PasswordSetView):
    success_url = reverse_lazy("dashboard")


settings_view = login_required(Settings.as_view())
