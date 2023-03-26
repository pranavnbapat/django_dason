from django.http import request
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.views.generic import TemplateView

User = get_user_model()
# class PagesView(LoginRequiredMixin, TemplateView):
class PagesView(TemplateView):
    pass


#  Authentication
pages_authentication_login_view = PagesView.as_view(
    template_name="pages/authentication/auth-login.html"
)
pages_authentication_register_view = PagesView.as_view(
    template_name="pages/authentication/auth-register.html"
)
pages_authentication_recoverpw_view = PagesView.as_view(
    template_name="pages/authentication/auth-recoverpw.html"
)
pages_authentication_lockscreen_view = PagesView.as_view(
    template_name="pages/authentication/auth-lock-screen.html"
)
pages_authentication_logout_view = PagesView.as_view(
    template_name="pages/authentication/auth-logout.html"
)
pages_authentication_confirm_mail_view = PagesView.as_view(
    template_name="pages/authentication/auth-confirm-mail.html"
)
pages_authentication_email_verification_view = PagesView.as_view(
    template_name="pages/authentication/auth-email-verification.html"
)
pages_authentication_two_step_verification_view = PagesView.as_view(
    template_name="pages/authentication/auth-two-step-verification.html"
)