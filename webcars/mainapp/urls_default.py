
from django.conf.urls import url
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from registration.backends.default.views import RegistrationView
from mainapp.forms import MyRegForm
from mainapp import views as main_views


class RegistrationViewUniqueEmail(RegistrationView):
    form_class = MyRegForm

urlpatterns = [

    path('', main_views.index, name='index'),

    url(r'^register/$', RegistrationViewUniqueEmail.as_view(),
        name='registration_register'),

    url(r'^accounts/',
        include('registration.backends.default.urls')),

    url(r'^accounts/profile/',
        TemplateView.as_view(template_name='profile.html'),
        name='profile'),

    url(r'^login/',
        auth_views.login,
        name='login'),

    url(r'^admin/',
        admin.site.urls,
        name='admin'),

]
