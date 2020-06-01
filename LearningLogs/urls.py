# urls of app

from django.conf.urls import url

from . import views

urlpatterns = [
    # Home page
    url(r'^$', views.index, name='index'),

    # Page with topics
    url(r'^topics/$', views.topics, name='topics'),

    # Page for single topic
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic')
]