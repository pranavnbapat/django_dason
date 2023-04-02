from .mixins import AdminMenuMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from ..forms import MyFormForm
from django.shortcuts import render, redirect
from .context_processors import get_countries
from django.contrib.auth.hashers import make_password
from .data_processing import manage_avatar_upload
from django.contrib import messages


class FormView(LoginRequiredMixin, TemplateView, AdminMenuMixin):
    template_name = "backend/forms/form.html"

    def get(self, request, *args, **kwargs):
        form = MyFormForm()
        context = self.get_context_data(form=form)
        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_countries())
        return context

    def post(self, request):
        form = MyFormForm(request.POST, request.FILES)

        if form.is_valid():
            form_data = form.save(commit=False)

            # This needs to be tested
            password = make_password(request.POST.get('password'))
            form_data.password = password
            # This needs to be tested

            if request.FILES['avatar']:
                file = request.FILES['avatar']
                avatar = manage_avatar_upload(file)
                form_data.avatar = avatar

            form_data.save()
            messages.success(request, "Form data saved successfully.")
            return redirect('backend:my_form')
        else:
            messages.error(request, "There was an error processing the form.")
            context = self.get_context_data(form=form)
            return render(request, self.template_name, context)

