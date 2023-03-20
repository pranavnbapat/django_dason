from django.contrib.auth import get_user_model
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import MyForm
from django.views.decorators.http import require_POST


class FormView(TemplateView):
    template_name = "backend/forms/form.html"
    success_url = reverse_lazy("backend:my_form")

    def get(self, request, *args, **kwargs):
        # Pass the form data in the context if it exists
        context = self.get_context_data(**kwargs)
        print(context)
        context['form_data'] = request.POST.copy()
        print(context)
        # context['form_data'] = request.POST if 'form_data' in request.POST else None
        return self.render_to_response(context)

    def post(self, request):
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')

        # Print post data
        # for key, value in request.POST.items():
        #     print('Key: %s' % (key))
        #     # print(f'Key: {key}') in Python >= 3.7
        #     print('Value %s' % (value))
        #     # print(f'Value: {value}') in Python >= 3.7

        # Validate form inputs
        # if not fname or not lname or not email or not gender or not dob:
        #     messages.error(request, 'All fields are required.')
        #     form_data = request.POST.copy()
        #     return render(request, self.template_name, {'form_data': form_data})

        try:
            form_data = MyForm(fname=fname, lname=lname, email=email, gender=gender, dob=dob)
            form_data.save()
            messages.success(request, "Form data saved successfully.")
            return redirect('backend:my_form')
        except Exception as e:
            # print(e)
            messages.error(request, e)
            return redirect('backend:my_form')


class ProfileView(TemplateView):
    template_name = "backend/user/profile.html"


# Forms
form_view = login_required(FormView.as_view())

# User profile
profile_view = login_required(ProfileView.as_view())

