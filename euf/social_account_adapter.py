from allauth_2fa.adapter import OTPAdapter


class SocialAccountAdapter(OTPAdapter):
    def get_login_redirect_url(self, request):
        # Add your custom logic here to determine the redirect URL
        # For example, you can return a hardcoded URL or get it from the request object
        return '/backend/dashboard'
