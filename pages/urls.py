from django.urls import path

from .views import (
    pages_authentication_login_view,
    pages_authentication_register_view,
    pages_authentication_recoverpw_view,
    pages_authentication_lockscreen_view,
    pages_authentication_logout_view,
    pages_authentication_confirm_mail_view,
    pages_authentication_email_verification_view,
    pages_authentication_two_step_verification_view,
)

app_name = "pages"

urlpatterns = [
    # Authentication
    path(
        "authentication/login",
        view=pages_authentication_login_view,
        name="pages.authentication.login",
    ),
    path(
        "authentication/register",
        view=pages_authentication_register_view,
        name="pages.authentication.register",
    ),
    path(
        "authentication/recoverpw",
        view=pages_authentication_recoverpw_view,
        name="pages.authentication.recoverpw",
    ),
    path(
        "authentication/lock-screen",
        view=pages_authentication_lockscreen_view,
        name="pages.authentication.lockscreen",
    ),
    path(
        "authentication/logout",
        view=pages_authentication_logout_view,
        name="pages.authentication.logout",
    ),
    path(
        "authentication/confirm_mail",
        view=pages_authentication_confirm_mail_view,
        name="pages.authentication.confirm_mail",
    ),
    path(
        "forms/email_verification",
        view=pages_authentication_email_verification_view,
        name="pages.authentication.email_verification",
    ),
    path(
        "forms/two_step_verification",
        view=pages_authentication_two_step_verification_view,
        name="pages.authentication.two_step_verification",
    ),
]
