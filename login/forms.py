from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, SetPasswordForm


class SignupForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput())
    password2 = forms.CharField(
        label='Confirm Password', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']
        labels = {'email': 'Email'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # List of field names you want to add a class to
        fields_to_add_class = ['first_name', 'last_name',
                               'username', 'email', 'password1', 'password2']

        # Add the 'form-control' to each field in the list
        for field_name in fields_to_add_class:
            self.fields[field_name].widget.attrs['class'] = 'form-control'


class LoginForm(AuthenticationForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # List of field names you want to add a class to
        fields_to_add_class = ['username', 'password']

        # Add the 'form-control' to each field in the list
        for field_name in fields_to_add_class:
            self.fields[field_name].widget.attrs['class'] = 'form-control'


class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(
        label='Old Password', widget=forms.PasswordInput())
    new_password1 = forms.CharField(
        label='New Password', widget=forms.PasswordInput())
    new_password2 = forms.CharField(
        label='Confirm New Password', widget=forms.PasswordInput())

    class Meta:
        model = User

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # List of field names you want to add a class to
        fields_to_add_class = ['old_password',
                               'new_password1', 'new_password2']

        # Add the 'form-control' to each field in the list
        for field_name in fields_to_add_class:
            self.fields[field_name].widget.attrs['class'] = 'form-control'


class ChangePasswordForm1(SetPasswordForm):
    new_password1 = forms.CharField(
        label='New Password', widget=forms.PasswordInput())
    new_password2 = forms.CharField(
        label='Confirm New Password', widget=forms.PasswordInput())

    class Meta:
        model = User

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # List of field names you want to add a class to
        fields_to_add_class = ['new_password1', 'new_password2']

        # Add the 'form-control' to each field in the list
        for field_name in fields_to_add_class:
            self.fields[field_name].widget.attrs['class'] = 'form-control'
