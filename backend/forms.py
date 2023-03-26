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
        }
