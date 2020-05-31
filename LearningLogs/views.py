from django.shortcuts import render
from .models import Topic
# Create your views here.


def index(request):
    """Displaying home page"""
    return render(request, 'LearningLogs/index.html')


def topics(request):
    """Displaying page with topics"""
    topics = Topic.objects.order_by('posted_date')
    context = {'topics': topics}
    return render(request, 'LearningLogs/topics.html', context)
