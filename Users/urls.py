"""Defining urls templates for User app"""

from django.conf.urls import url
from django.contrib.auth.views import LoginView
from . import views


urlpatterns = [
    # Login page
    url(r'^login/$', LoginView.as_view(template_name='Users/login.html'), name='login'),
    url(r'^logout$', view=views.logout_view, name='logout'),
    url(r'^register/$', view=views.register, name='register')
]