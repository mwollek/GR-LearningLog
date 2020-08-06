from django.shortcuts import render
from .models import Topic, Entry, Test
from .forms import TopicForm, EntryForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    """Displays home page"""
    return render(request, 'LearningLogs/index.html')


@login_required
def topics(request):
    """Displays page with topics"""
    topics = Topic.objects.order_by('posted_date')
    context = {'topics': topics}
    return render(request, 'LearningLogs/topics.html', context)


@login_required
def topic(request, topic_id):
    """Displays single topic and conected entries"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-posted_date')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'LearningLogs/topic.html', context)


@login_required
def new_topic(request):
    """Creates form for new topic, or import new topic to database"""
    if request.method != 'POST':
        # No data has been given so new form has to be created.
        form = TopicForm()
    else:
        # Data has been given as POST request, it has to be processed
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('LearningLogs:topics'))
    context = {'form': form}
    return render(request, 'LearningLogs/new_topic.html', context)


@login_required
def new_entry(request, topic_id):
    """Creates form for new entry connected with topic -> topic_id"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('LearningLogs:topic', args=[topic_id]))

    context = {'topic': topic, 'form': form}
    return render(request, 'LearningLogs/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    """Editing form"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('LearningLogs:topic', args=[topic.id]))
    context = {'topic': topic, 'entry': entry, 'form': form}
    return render(request, 'LearningLogs/edit_entry.html', context)
