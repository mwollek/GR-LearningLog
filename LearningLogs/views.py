from django.shortcuts import render
from .models import Topic
# Create your views here.


def index(request):
    """Displays home page"""
    return render(request, 'LearningLogs/index.html')


def topics(request):
    """Displays page with topics"""
    topics = Topic.objects.order_by('posted_date')
    context = {'topics': topics}
    return render(request, 'LearningLogs/topics.html', context)


def topic(request, topic_id):
    """Displays single topic and conected entries"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-posted_date')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'LearningLogs/topic.html', context)