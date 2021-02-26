from django.http import HttpResponse
from django.shortcuts import redirect


#once logged in will not let user got to register
def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('issue_tracker:home')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func
