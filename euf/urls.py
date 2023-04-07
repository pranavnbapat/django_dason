from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from euf import views
from django.views.generic import RedirectView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),

    path("settings", views.Settings.as_view(), name="settings"),

    # Custom change password done page redirect
    path(
        "account/password/change/",
        login_required(views.MyPasswordChangeView.as_view()),
        name="account_change_password",
    ),

    # Custom set password done page redirect
    path(
        "account/password/set/",
        login_required(views.MyPasswordSetView.as_view()),
        name="account_set_password",
    ),

    # Backend
    path("backend/", include("backend.urls")),

    # Pages
    path("pages/", include("pages.urls")),

    # Add the redirect for the '/account' URL
    path("account/", RedirectView.as_view(url="/account/login/?next=/", permanent=False), name="account_redirect"),

    # Include the allauth and 2FA urls from their respective packages.
    path("/", include("allauth_2fa.urls")),
    path("account/", include("allauth.urls")),

    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
