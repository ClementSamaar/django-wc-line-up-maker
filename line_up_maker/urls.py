"""line_up_maker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from wc_line_up_maker.views.authentication import UserLoginView, logout_view
from wc_line_up_maker.views.formation import FormationListView, FormationDetailView, FormationFormView, \
    create_formation_template, FormationDeleteView
from wc_line_up_maker.views.index import IndexView
from wc_line_up_maker.views.line_up import LineUpFormView, \
    create_line_up_template, line_up_detail_view, line_up_list_view #LineUpListView, LineUpDetailView,
from wc_line_up_maker.views.register import RegisterFormView
from wc_line_up_maker.views.squad import SquadListView, SquadDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', RegisterFormView.as_view(), name='register_form'),
    path('login/', UserLoginView.as_view(), name='login_form'),
    path('logout/', logout_view, name='logout'),
    path('', IndexView.as_view(), name='index'),
    path('formation/', FormationListView.as_view(), name='formation_list'),
    path('formation/create/', FormationFormView.as_view(), name='formation_form'),
    path('formation/delete/<int:pk>', FormationDeleteView.as_view(), name='formation_delete'),
    path('formation/template/create/<int:pk>', create_formation_template, name='formation_template_form'),
    path('formation/<int:pk>', FormationDetailView.as_view(), name='formation'),
    path('squad/', SquadListView.as_view(), name='squad_list'),
    path('squad/<int:pk>', SquadDetailView.as_view(), name='squad'),
    # path('line_up/', LineUpListView.as_view(), name='line_up_list'),
    # path('line_up/<int:pk>', LineUpDetailView.as_view(), name='line_up'),
    path('line_up/', line_up_list_view, name='line_up_list'),
    path('line_up/<int:pk>', line_up_detail_view, name='line_up'),
    path('line_up/create/', LineUpFormView.as_view(), name='line_up_form'),
    path('line_up/template/create/<int:pk>', create_line_up_template, name='line_up_template_form')
]
