from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.contrib.auth.models import User
from .models import Profile


def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'users/profiles.html', context)


def profile(request, pk):
    profile = Profile.objects.get(uuid=pk)

    top_skills = profile.skill_set.exclude(description="")
    other_skills = profile.skill_set.filter(description="")

    context = {'profile': profile, 'top_skills': top_skills,
               'other_skills': other_skills}
    return render(request, 'users/profile.html', context)


def loginUser(request):
    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'This user does not exist.')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            redirect('profiles')
        else:
            messages.error(request, 'Your username or password are incorrect.')

    return render(request, 'users/login_form.html')


@login_required
def logoutUser(request):
    logout(request)
    messages.error(request, "You've been logged out.")
    return redirect('login')
