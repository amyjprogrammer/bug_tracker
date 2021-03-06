from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import Group

from .forms import CreateUserForm, UserUpdateForm
from .decorators import unauthenticated_user


@unauthenticated_user
def register(request):
    """creating a new account"""
    if request.method != 'POST':
        #empty form for someone to register
        form = CreateUserForm()
    else:
        #completed the info and setting up an account
        form = CreateUserForm(data=request.POST)
        if form.is_valid():
            user = form.save()

            group = Group.objects.get(name='customer')
            user.groups.add(group)

            messages.success(request,f'Your account had been created!')
            return redirect('login')

    context = {'form': form}
    return render(request, 'users/register.html', context)

def profile(request):
    if request.method != 'POST':
        #show the user info
        form = UserUpdateForm(instance=request.user)
    else:
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been updated.')
            return redirect('profile')

    context = {'form': form}
    return render(request, 'users/profile.html', context)
