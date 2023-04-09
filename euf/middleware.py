from backend.models import UserActivityLog
from django.utils import timezone


class UserActivityMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        user = request.user
        if user.is_authenticated:
            method = request.method
            activity = request.path
            log_entry = UserActivityLog(user=user, method=method, activity=activity, timestamp=timezone.now())
            log_entry.save()

        return response
