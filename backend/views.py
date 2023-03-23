from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import MyForm


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

        self.post_data = request.POST.dict()

        try:
            form_data = MyForm(fname=fname, lname=lname, email=email, gender=gender, dob=dob)
            form_data.full_clean()
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
