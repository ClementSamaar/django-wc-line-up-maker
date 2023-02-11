from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.views.generic import FormView

from wc_line_up_maker.form.register import RegisterForm


class RegisterFormView(FormView):
    form_class = RegisterForm
    template_name = 'register_form.html'

    def form_valid(self, form):
        user = User.objects.create(email=form.cleaned_data['email'],
                                   username=form.cleaned_data['username'],
                                   password=make_password(form.cleaned_data['password']))

        return HttpResponseRedirect('/')
