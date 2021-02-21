from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import UserCreationForm

from .forms import CreateUserForm

def register(request):
    """creating a new account"""
    if request.method != 'POST':
        #empty form for someone to register
        form = CreateUserForm()
    else:
        #completed the info and setting up an account
        form = CreateUserForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {'form': form}
    return render(request, 'users/register.html', context)
