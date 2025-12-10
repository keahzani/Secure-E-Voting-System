from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import Group
from .forms import UserRegisterForm
from .models import Profile
from elections.models import Election
from voting.models import Vote
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            id_number = form.cleaned_data.get('identification_number')
            role = form.cleaned_data.get('role')

            # Profile is auto-created by signal; update fields:
            profile = user.profile
            profile.role = role
            profile.identification_number = id_number
            profile.save()
        
            # Assign group automatically based on role
            if role == 'admin':
                group = Group.objects.get(name='Admin')
            elif role == 'officer':
                group = Group.objects.get(name='Election Officer')
            else:
                group = Group.objects.get(name='Voter')

            user.groups.add(group)
            
            messages.success(request, f'Account created for {user.username}!')
            return redirect('login')
        else:
            print("⚠️ Form errors:", form.errors)
    else:
        form = UserRegisterForm() 
    return render(request, 'users/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # We'll define this later
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'users/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

def home(request):
    return render(request, 'home.html')

@login_required
def dashboard(request):
    user = request.user
    current_time = now()

    # All elections happening now
    active_elections = Election.objects.filter(start_time__lte=current_time, end_time__gte=current_time)

    # Elections the user has already voted in
    voted_elections = Election.objects.filter(vote__voter=user)

@login_required
def dashboard(request):
    user = request.user
    current_time = now()

    # Active elections within date range
    active_elections = Election.objects.filter(start_date__lte=current_time, end_date__gte=current_time)

    # Elections the user has voted in
    voted_elections = Election.objects.filter(vote__voter=user)

    # Eligible elections = active and not yet voted
    eligible_elections = active_elections.exclude(id__in=voted_elections.values_list('id', flat=True))

    context = {
        'user': user,
        'eligible_elections': eligible_elections,
        'voted_elections': voted_elections,
    }

    return render(request, 'users/dashboard.html', context)
