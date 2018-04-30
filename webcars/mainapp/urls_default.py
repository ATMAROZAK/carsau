from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from registration.backends.default.views import RegistrationView
from mainapp.forms import MyRegForm


class RegistrationViewUniqueEmail(RegistrationView):
    form_class = MyRegForm

urlpatterns = [

    url(r'^$',
        TemplateView.as_view(template_name='index.html'),
        name='index'),

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
