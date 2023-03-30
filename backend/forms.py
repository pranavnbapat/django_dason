from django import forms
from .models import MyForm


class MyFormForm(forms.ModelForm):
    class Meta:
        model = MyForm
        fields = ['fname', 'lname', 'email', 'gender', 'dob', 'descr', 'avatar', 'contact_no', 'countries_master_id']
        widgets = {
            'fname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name', 'maxlength': '50',
                                            'pattern': '[a-zA-Z\s]+$'}),
            'lname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name',
                                            'pattern': '[a-zA-Z\s]+$', 'maxlength': '50'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email', 'maxlength': '50'}),
            'contact_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact Number',
                                                 'pattern': '[0-9-\s]+$', 'maxlength': '15'}),
            # 'countries_master_id': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.errors.get('email'):
            email_widget = self.fields['email'].widget
            email_widget.attrs.update({'class': email_widget.attrs['class'] + ' is-invalid'})
            self.fields['email'].widget.attrs.update({'style': 'border-color: #ef6767;'})

        if self.errors.get('fname'):
            email_widget = self.fields['fname'].widget
            email_widget.attrs.update({'class': email_widget.attrs['class'] + ' is-invalid'})
            self.fields['fname'].widget.attrs.update({'style': 'border-color: #ef6767;'})

        if self.errors.get('lname'):
            email_widget = self.fields['lname'].widget
            email_widget.attrs.update({'class': email_widget.attrs['class'] + ' is-invalid'})
            self.fields['lname'].widget.attrs.update({'style': 'border-color: #ef6767;'})

        if self.errors.get('contact_no'):
            email_widget = self.fields['contact_no'].widget
            email_widget.attrs.update({'class': email_widget.attrs['class'] + ' is-invalid'})
            self.fields['contact_no'].widget.attrs.update({'style': 'border-color: #ef6767;'})
