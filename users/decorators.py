from django.http import HttpResponseForbidden
from django.shortcuts import redirect
from functools import wraps

def admin_required(function):
    def wrap(request, *args, **kwargs):
        if not request.user.groups.filter(name='Admin').exists():
            return HttpResponseForbidden("You are not authorized to view this page.")
        return function(request, *args, **kwargs)
    return wrap

def election_officer_required(function):
    def wrap(request, *args, **kwargs):
        if not request.user.groups.filter(name='Election Officer').exists():
            return HttpResponseForbidden("You are not authorized to view this page.")
        return function(request, *args, **kwargs)
    return wrap

def voter_required(function):
    def wrap(request, *args, **kwargs):
        if not request.user.groups.filter(name='Voter').exists():
            return HttpResponseForbidden("You are not authorized to view this page.")
        return function(request, *args, **kwargs)
    return wrap

def admin_or_officer_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated and hasattr(request.user, 'profile'):
            role = request.user.profile.role
            if request.user.groups.filter(name__in=['Admin', 'Election Officer']).exists():
                return view_func(request, *args, **kwargs)
        return HttpResponseForbidden("You are not authorized to view this page.")
    return wrapper