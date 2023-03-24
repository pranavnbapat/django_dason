from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import MyForm
from django.conf import settings
import os
import string
import random


def generate_random_filename(length: int):
    """Generate a random alphanumeric filename with the specified length."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


class FormView(TemplateView):
    template_name = "backend/forms/form.html"

    post_data = {}

    # Populate fields on page load
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['post_data'] = self.post_data
    #     return context

    def post(self, request):
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        descr = request.POST.get('descr')
        avatar = ""

        if request.FILES.get('avatar'):
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

        self.post_data = request.POST.dict()

        form_data = MyForm(fname=fname, lname=lname, email=email, gender=gender, dob=dob, descr=descr, avatar=avatar)

        try:
            form_data.save()
            messages.success(request, "Form data saved successfully.")
            return redirect('backend:my_form')
        except Exception as e:
            messages.error(request, e)
            return render(request, 'backend/forms/form.html', {'post_data': self.post_data})


class ProfileView(TemplateView):
    template_name = "backend/user/profile.html"


# Forms
form_view = login_required(FormView.as_view())

# User profile
profile_view = login_required(ProfileView.as_view())
