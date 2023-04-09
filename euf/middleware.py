from django.utils import timezone
from backend.models import UserActivityLog


class UserActivityMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        user = request.user
        if user.is_authenticated:
            method = request.method
            activity = request.path
            user_timezone = request.COOKIES.get('user_timezone', 'UTC')  # Get the user's timezone from the cookie
            log_entry = UserActivityLog(user=user, method=method, activity=activity, timestamp=timezone.now(), user_timezone=user_timezone)
            log_entry.save()

        return response
