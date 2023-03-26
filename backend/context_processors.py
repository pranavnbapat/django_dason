def greeting(request):
    context_data = {
        'greeting': 'Hello, world!',
    }
    return context_data
