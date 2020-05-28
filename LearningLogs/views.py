from django.shortcuts import render

# Create your views here.

def index(request):
    """Define view for main page"""

    return render(request, 'LearningLogs/index.html')