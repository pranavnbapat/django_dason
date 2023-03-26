from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from django.conf import settings
import os
import string
import random
from .context_processors import greeting
from .forms import MyFormForm


def generate_random_filename(length: int):
    """Generate a random alphanumeric filename with the specified length."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


class FormView(TemplateView):
    template_name = "backend/forms/form.html"

    def get(self, request, *args, **kwargs):
        form = MyFormForm()
        custom_context = greeting(request)
        context = {'form': form}
        context.update(custom_context)
        return render(request, self.template_name, context)

    def post(self, request):
        form = MyFormForm(request.POST, request.FILES)

        if form.is_valid():
            form_data = form.save(commit=False)

            if form_data.avatar:
                file = request.FILES['avatar']
                # Ensure the AVATAR_PATH exists
                os.makedirs(settings.AVATAR_PATH, exist_ok=True)

                # Generate a random alphanumeric filename
                random_filename = generate_random_filename(length=20)

                # Remove the extension of the file and store it
                _, file_ext = os.path.splitext(file.name)

                avatar = random_filename + file_ext

                with open(os.path.join(settings.AVATAR_PATH, avatar), 'wb+') as destination:
                    for chunk in file.chunks():
                        destination.write(chunk)

            form_data.save()
            messages.success(request, "Form data saved successfully.")
            return redirect('backend:my_form')
        else:
            messages.error(request, "There was an error processing the form.")
            return render(request, 'backend/forms/form.html', {'form': form})


class ProfileView(TemplateView):
    template_name = "backend/user/profile.html"


# Forms
form_view = login_required(FormView.as_view())

# User profile
profile_view = login_required(ProfileView.as_view())
