from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views import View
from django.urls import reverse_lazy
from allauth.account.views import PasswordSetView, PasswordChangeView
from django_otp.plugins.otp_totp.models import TOTPDevice
from backend.views.mixins import AdminMenuMixin
from django.http import HttpResponse
from django.core.cache import cache
import datetime


def home(req):
    return render(req, "frontend/home.html")


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
    success_url = reverse_lazy("backend:dashboard")


class MyPasswordSetView(LoginRequiredMixin, PasswordSetView):
    success_url = reverse_lazy("dashboard:dashboard")


settings_view = login_required(Settings.as_view())


def test_cache(request):
    cached_value = cache.get("test_key")

    if cached_value is None:
        now = datetime.datetime.now()
        cached_value = f"This value was cached at {now}"
        cache.set("test_key", cached_value, timeout=60)  # Cache the value for 1 minute

    return HttpResponse(cached_value)
