from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.urls import reverse

from wc_line_up_maker.views.index import IndexView


class UserLoginView(LoginView):
    next_page = 'index'
    template_name = 'login.html'


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
