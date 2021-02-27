from django.http import HttpResponse
from django.shortcuts import redirect


def allowed_users(allowed_groups=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.filter(name__in=allowed_groups).exists():
                #user is in one of the allowed groups
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You are not authorized to view this page.')
        return wrapper_func
    return decorator

def admin_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'customer':
            return redirect('issue_tracker:user_page')

        if group == 'admin':
            return view_func(request, *args, **kwargs)

    return wrapper_func
