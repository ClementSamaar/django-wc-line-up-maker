from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.Form):
    email = forms.CharField(max_length=200, required=True)
    username = forms.CharField(max_length=200, required=True)
    password = forms.CharField(max_length=200, required=True, widget=forms.PasswordInput)
    password_validation = forms.CharField(max_length=200, required=True, widget=forms.PasswordInput)

    def clean(self):
        for registered_user in User.objects.all():
            if registered_user.username == self.cleaned_data['username']:
                self.add_error('username',
                               'There is already a user with this username, please choose a different username')
            if registered_user.email == self.cleaned_data['email']:
                self.add_error('email',
                               'An account with this email already exists, please use another email')
        if self.cleaned_data['password'] != self.cleaned_data['password_validation']:
            self.add_error('password', 'The password inputs are different')
        return self.cleaned_data
