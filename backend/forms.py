from django import forms
from .models import MyForm


class MyFormForm(forms.ModelForm):
    class Meta:
        model = MyForm
        fields = ['fname', 'lname', 'email', 'gender', 'dob', 'descr', 'avatar']
        widgets = {
            'fname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'lname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name',
                                            'pattern': '[a-zA-Z\s]+'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.errors.get('email'):
            email_widget = self.fields['email'].widget
            email_widget.attrs.update({'class': email_widget.attrs['class'] + ' is-invalid'})
