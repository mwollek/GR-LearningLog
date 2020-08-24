from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
# Create your views here.


def logout_view(request):
    """ Logout function """
    logout(request)
    return HttpResponseRedirect(reverse('LearningLogs:index'))


def register(request):
    """Displays a register page, where user can create an account"""
    if request.method != 'POST':
        form = UserCreationForm()

    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            authenticated_user = authenticate(username = new_user.username, password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('LearningLogs:index'))
    context = {'form': form}
    return render(request, 'Users/register.html', context)
