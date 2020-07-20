# urls of app

from django.conf.urls import url

from . import views

urlpatterns = [
    # Home page
    url(r'^$', view=views.index, name='index'),

    # Page with topics
    url(r'^topics/$', view=views.topics, name='topics'),

    # Page for single topic
    url(r'^topics/(?P<topic_id>\d+)/$', view=views.topic, name='topic'),

    # Page for adding topic
    url(r'^new_topic/$', view=views.new_topic, name='new_topic'),

    # Page for adding entry for topic
    url(r'^new_entry/(?P<topic_id>\d+)/$', view=views.new_entry, name='new_entry'),

    # Page for editing entries
    url(r'^edit_entry/(?P<entry_id>\d+)/$', view=views.edit_entry, name='edit_entry'),

]