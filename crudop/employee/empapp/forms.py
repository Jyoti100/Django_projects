from django import forms
from .models import Employee
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        #fields = '__all__'
        fields = ['empname', 'empemail', 'empcontact']

class Signupform(UserCreationForm):
    name = forms.CharField(max_length=50)
    last_name=forms.CharField(max_length=50)
    email = forms.EmailField(max_length=250, help_text="Enter a valid Email Address")

    class Meta:
        model = User
        fields=('username', 'name', 'last_name', 'email', 'password1', 'password2', )

