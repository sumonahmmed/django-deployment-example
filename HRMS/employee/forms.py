from django import forms
from django.contrib.auth.models import User
from employee.models import BranchDetails, EmployeeInput, Userprofile


class BranchDetailsForms(forms.ModelForm):
    class Meta():
        model = BranchDetails
        fields = '__all__'


class EmployeeInputForms(forms.ModelForm):
    class Meta():
        model = EmployeeInput
        fields = '__all__'


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    class Meta():
        model = Userprofile
        fields = ('portfolio', 'profile_picture')