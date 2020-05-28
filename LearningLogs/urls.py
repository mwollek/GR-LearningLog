""" Define mocks of URL for LearningLogs application"""

from django.conf.urls import url

from . import views

urlpatterns = [
    # Main page
    url(r'^$', views.index, name='index')
]