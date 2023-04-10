from datetime import timedelta


def custom_lockout_time(request, credentials, **kwargs):
    # Get the number of failed login attempts from kwargs
    attempts = kwargs.get("attempts", 0)

    # Define the lockout durations based on the number of failed attempts
    if attempts > 5:
        return timedelta(hours=24)
    elif attempts == 5:
        return timedelta(hours=1)
    elif attempts == 3:
        return timedelta(minutes=5)
    else:
        return None
